import os    
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Tkplus:
 
    root = Tk()

    def __init__(self, width:int=300, height:int=300, 
                 title:str="tkplus", icon:str="tkplus_img", 
                 **kwargs):

        self.width = width
        self.height = height

        self.openfile = askopenfilename
        self.savefile = asksaveasfilename
 
        try:
                self.root.wm_iconbitmap(icon) 
        except:
                pass
 
        try:
            self.width = kwargs['width']
        except KeyError:
            pass
 
        try:
            self.height = kwargs['height']
        except KeyError:
            pass
 
        self.root.title(title)
 
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
     
        left = (screenWidth / 2) - (self.width / 2) 
         
        top = (screenHeight / 2) - (self.height /2) 
         
        self.root.geometry('%dx%d+%d+%d' % (self.width,
                                              self.height,
                                              left, top)) 

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)    

    def element(self, elem: str=None, elemattr: str=None, elemattr2: str=None):

        elem = elem.lower()
        elemattr = elem.lower()

        if elem == "text":
            text = Text(self.root)
            self.text = text
            self.text.grid(sticky = N + E + S + W)
            return self.text

        elif elem == "scrollbar": 
            scrollbar = Scrollbar(self.root)
            self.scrollbar = scrollbar
            self.scrollbar.pack(side=RIGHT,fill=Y)                
            self.scrollbar.config(command=self.root.yview)
            return self.scrollbar

    def kill(self):
        self.root.destroy()
 
    def run(self):
        self.root.mainloop()
    
def demo():
    root = Tkplus()
    root.element(elem="text", elemattr="root")
    root.run()

if __name__ == "__main__":
    demo()