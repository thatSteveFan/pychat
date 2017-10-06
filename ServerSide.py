from socket import *
from threading import *
from queue import *

class InputThread(Thread):
	def __init__(self, socket, queue_to_push_to):
		super(InputThread, self).__init__(name = "Input" + str(socket.getsockname()))
		self._queue = queue_to_push_to
		self._socket = socket
		self._running = True;
		
	def run(self):
		while(self._running):
			input = (self._socket.recv(1024).decode())
			if input:
				print(input)
				self._queue.put(input)
			else:
				self._running = False
	def stop(self):
		self._running = False
				
class OutputThread(Thread):
	def __init__(self, socket):
		super(OutputThread, self).__init__(name = "Output" + str(socket.getsockname()))
		self._queue = Queue()
		self._socket = socket
		self._running = True
	
	def run(self):
		while(self._running):
			out = self._queue.get().encode()
			print(self._socket, out)
			print(self._socket.send(out))
	def stop(self):
		self._running = False
	def out(self, out):
		self._queue.put(out)
		
		
class DriverThread(Thread):
	def __init__(self, in_queue, outthreads):
		super().__init__(name = "Driver")
		self.queue = in_queue
		self.outs = outthreads
		self.running = True
	def run(self):
		while(self.running):
			out = self.queue.get();
			
			for thread in self.outs:
				print(thread, out)
				thread.out(out)
		
	def stop(self):
		self.running = False
if __name__ == "__main__":
	
	s = socket(AF_INET, SOCK_STREAM)
	s.bind( ("0.0.0.0", 50000) )
	
	s.listen()
	input_queue = Queue()
	
	inthreads = []
	outthreads = []
	dt = DriverThread(input_queue, outthreads)
	dt.start()
	try:
		while(1):
			(conn, adress) = s.accept()
			it = InputThread(conn, input_queue)
			it.start()
			out = OutputThread(conn)
			outthreads.append(out)
			out.start()
	except KeyboardInterrupt:
		dt.stop()
		s.close()
	
