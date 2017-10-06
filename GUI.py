import tkinter as tk
from tkinter.ttk import *
from socket import *
import threading
class GUI:
		
	def __init__(self, connection):
		self_conn = connection
		self._root = tk.Tk()
		self._root.title("SCA (Simple Chat App)")
		
		text = tk.Text(self._root)
		text.pack(expand=tk.YES, fill=tk.BOTH)
		text.insert(tk.END, "initialized\n")
		text.config(state = tk.DISABLED)
		
		entry = MultilineEntry(self._root)
		
		def sendhandler(event):
			s.send(event.widget.clear_and_get().encode())
		def rcvhandler(str):
			print("handling", str)
			text.config(state = tk.NORMAL)
			text.insert(tk.END, str)
			text.config(state = tk.DISABLED)
		self.rcv_handler = rcvhandler
		entry.bind("<Control-Return>", sendhandler)
		entry.pack(expand=tk.YES, fill=tk.BOTH)
		entry.bind()
		
		
	def start(self):
		self._root.mainloop()
		
class MultilineEntry(tk.Text):
	
	def retur(event):
		event.widget.clear_and_get()
	def __init__(self, master):
		super().__init__(master)
	def clear_and_get(self):
		text = self.get("0.0", tk.END)
		self.delete("0.0", tk.END)
		return text
	
class ReadThread(threading.Thread):
	def __init__(self, conn, callback):
		super().__init__(name = "reader")
		self.conn = conn
		self.callback = callback
	def run(self):
		print("Starting")
		while(1):
			print("started")
			input = self.conn.recv(4096).decode()
			print(input)
			self.callback(input)
		
if __name__ == "__main__":
	s = socket()
	s.connect(("localhost", 50000))
	gui = GUI(s)
	rt = ReadThread(s, gui.rcv_handler)
	rt.start()
	gui.start()