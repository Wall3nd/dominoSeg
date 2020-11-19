import socket

def joinTable():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', 50000))
	message = "Hello world"
	s.sendall(message.encode())
	data = s.recv(1024)
	s.close()
	print('Received', repr(data))

#def chooseInitialTiles():
	#

#def commitToHand():
	#

#def playTileFromHand():
	#

#def pickTile():
	#

#def checkTilesOnTheTable():
	#

#def checkWhoPlayedWhichTile():
	#

#def complainAgainstCheaters():
	#

#def acceptOutcome():
	#

#def cashPoints():
	#

joinTable()