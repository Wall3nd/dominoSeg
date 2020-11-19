import random
import select, socket, sys
import queue as Queue


class Domino:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return '[' + str(self.x) + '-' + str(self.y) + ']'

def allTiles():

	tilesList = []
	for i in range(7):
		for l in range(i,7):
			tilesList.append(Domino(i,l))
			#print(tilesList)

	return tilesList


def startingGame():
	
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setblocking(0)
	server.bind(('localhost', 50000))
	server.listen(5)
	inputs = [server]
	outputs = []
	message_queues = {}

	while inputs:
	    readable, writable, exceptional = select.select(
	        inputs, outputs, inputs)
	    for s in readable:
	        if s is server:
	            connection, client_address = s.accept()
	            connection.setblocking(0)
	            inputs.append(connection)
	            message_queues[connection] = Queue.Queue()
	        else:
	            data = s.recv(1024)
	            if data:
	                message_queues[s].put(data)
	                if s not in outputs:
	                    outputs.append(s)
	            else:
	                if s in outputs:
	                    outputs.remove(s)
	                inputs.remove(s)
	                s.close()
	                del message_queues[s]

	    for s in writable:
	        try:
	            next_msg = message_queues[s].get_nowait()
	        except Queue.Empty:
	            outputs.remove(s)
	        else:
	            s.send(next_msg)

	    for s in exceptional:
	        inputs.remove(s)
	        if s in outputs:
	            outputs.remove(s)
	        s.close()
	        del message_queues[s]

startingGame()