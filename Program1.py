from socket import *
from tkinter import *

class Application(Frame):
        def __init__(self, master):
            super(Application, self).__init__(master)
            self.grid()
            self.create_widgets()

        def create_widgets(self):
            Label(self,text = "IP ADDRESS FOUNDER").grid(row = 0,column = 0,sticky = W)
            self.txt = Entry(self)
            self.txt.grid(row = 1,column = 0,sticky = W)
            Button(self,text = "Find",command = self.findip).grid(row = 2,column = 0,sticky = W)
            self.t = Text(self)
            self.t.grid(row = 3,column = 0,sticky = W)

        def findip(self):
            host = self.txt.get()
            ip = gethostbyname(host)
            self.t.delete(0.0,END)
            self.t.insert(0.0, ip)
root = Tk()
root.title('Ip Address Finder')
root.geometry('300x250')
app = Application(root)
root.mainloop()