import tkinter as tk
from tkinter.ttk import *
class GUI:
	def __init__(self, connection):
		self_conn = connection
		self._root = tk.Tk()
		self._root.title("SCA (Simple Chat App)")
		
		text = tk.Text(self._root)
		text.pack(expand=tk.YES, fill=tk.BOTH)
		text.insert(tk.END, "initialized")
		#text.config(state = tk.DISABLED)
		
		entry = MultilineEntry(self._root)
		entry.bind("<Control-Return>", lambda x: text.insert(tk.END, x.widget.clear_and_get()))
		entry.pack(expand=tk.YES, fill=tk.BOTH)
		entry.bind()
		
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
	
		
		
if __name__ == "__main__":
	gui = GUI(None)