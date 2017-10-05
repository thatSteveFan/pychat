from socket import *
from threading import *


class InputThread(Thread):
	def __init__(self, socket):
		super(InputThread, self).__init__(name = "Input" + str(socket.getsockname()))
		self._socket = socket
		self._running = True;
		
	def run(self):
		while(self._running):
			input = (self._socket.recv(1024).decode())
			if input:
				print(input)
			else:
				self._running = False
	def stop(self):
		self._running = False
				
class OutputThread(Thread):
	def __init__(self, socket):
		super(OutputThread, self).__init__(name = "Output" + str(socket.getsockname()))
		self._socket = socket
		self._running = True;
		
	def run(self):
		while(self._running):
			out = input().encode()
			_socket.send(out)
	def stop(self):
		self._running = False
		
		
if __name__ == "__main__":
	print (input())	
	s = socket(AF_INET, SOCK_STREAM)
	s.bind( ("0.0.0.0", 50000) )
	
	s.listen()
	print(s)
	(conn, adress) = s.accept()
	it = InputThread(conn)
	it.start()
	out = OutputThread(conn)
	it.join()
	
	
