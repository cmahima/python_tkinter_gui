# Painting Application using tkinter python

from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox



class Paint:

    def __init__(self, root):
        self.chosen_color=("white","black")
        self.prev=Event()
        self.prev1 = Event()
        self.x1= 0.0
        self.y1=0.0
        self.x2= 0.0
        self.y2=0.0
        self.clicks=2
        self.rect=0
        self.oval=0
        self.line=0
        self.freeline=0
        root.title('Paint your Canvas')

        self.style = ttk.Style()
        self.style.configure('TLabel', background='#e1d8b9', font=('Arial', 20))
        '''
        self.frame= ttk.Frame(root)
        self.frame.pack()'''

        self.panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
        self.panedwindow.pack(fill=BOTH, expand=True)

        self.frame1 = ttk.Frame(self.panedwindow, width=100, height=300, relief=SUNKEN)
        self.frame2 = ttk.Frame(self.panedwindow, width=400, height=400, relief=SUNKEN)
        self.panedwindow.add(self.frame1, weight=1)
        self.panedwindow.add(self.frame2, weight=4)

        self.canvas=Canvas(self.frame2,width=1300, height=11200,
                background = 'white')
        self.canvas.grid(sticky='nwes')
        ttk.Button(self.frame1, text='Select Color',
                   command=self.color).grid(row=0, column=0, ipadx=5, ipady=5,sticky = 'e')
        ttk.Button(self.frame1, text='Draw Freehand',
                   command=self.click_draw).grid(row=1,ipadx=5, ipady=5,column=0,sticky = 'e')
        ttk.Button(self.frame1, text='Draw Rectangle',
                   command=self.click_rect).grid(row=2,ipadx=5, ipady=5,column=0,sticky = 'e')
        ttk.Button(self.frame1, text='Draw Oval',
                   command=self.click_oval).grid(row=3,ipadx=5, ipady=5,column=0,sticky = 'e')
        ttk.Button(self.frame1, text='Draw Line',
                   command=self.click_line).grid(row=4,ipadx=5, ipady=5,column=0,sticky = 'e')
        ttk.Button(self.frame1, text='Delete',
                   command=self.delete).grid(row=5,ipadx=5, ipady=5,column=0,sticky = 'e')

        self.canvas.bind('<ButtonPress>', self.mouse_press)


    def color(self):
        self.chosen_color=colorchooser.askcolor(initialcolor="#FFFFFF")

    def draw(self,event):
        self.freeline=self.canvas.create_line(self.prev.x, self.prev.y, event.x, event.y, width=5, fill=str(self.chosen_color[1]))
        self.prev = event

    def mouse_press(self,event):
         self.prev = event

    def click_draw(self):
        self.canvas.bind('<B1-Motion>', self.draw)

    def rectangle(self,event):
        print(event)
        print(self.prev1)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        print("{}:{}".format(x, y))
        self.canvas.create_oval((x - 1, y - 1, x + 1, y + 1), fill='black')
        self.rect = self.canvas.create_rectangle(self.prev1.x, self.prev1.y, event.x, event.y)
        self.canvas.unbind('<B1-ButtonRelease>')
        self.rect_color=(messagebox.askyesno(title = 'Color', message = 'Want to color the rectangle?'))
        if (self.rect_color==True):
            self.color()
            self.canvas.itemconfigure(self.rect, fill=str(self.chosen_color[1]))


    def click_rect(self):
        messagebox.showinfo(title="Mark the rectangle", message='Mark two points on the canvas to make the rectangle')
        self.canvas.bind('<B1-ButtonRelease>', self.mouse_rel)


    def mouse_rel(self,event):
         self.prev1 = event
         self.canvas.bind('<B1-ButtonRelease>', self.rectangle)
         x = self.canvas.canvasx(event.x)
         y = self.canvas.canvasy(event.y)
         print("{}:{}".format(x, y))
         self.canvas.create_oval((x - 1, y - 1, x + 1, y + 1), fill='black')

    def oval_make(self, event):
        print(event)
        print(self.prev1)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.create_oval((x - 1, y - 1, x + 1, y + 1), fill='black')
        self.oval = self.canvas.create_oval(self.prev1.x, self.prev1.y, event.x, event.y)
        self.canvas.unbind('<B1-ButtonRelease>')
        self.rect_color = (messagebox.askyesno(title='Color', message='Want to color the oval?'))
        if (self.rect_color == True):
            self.color()
            self.canvas.itemconfigure(self.oval, fill=str(self.chosen_color[1]))

    def click_oval(self):
        messagebox.showinfo(title="Mark the oval", message='Mark two points on the canvas to make the oval')
        self.canvas.bind('<B1-ButtonRelease>', self.mouse_rel_oval)

    def mouse_rel_oval(self,event):
         self.prev1 = event
         self.canvas.bind('<B1-ButtonRelease>', self.oval_make)
         x = self.canvas.canvasx(event.x)
         y = self.canvas.canvasy(event.y)
         self.canvas.create_oval((x - 1, y - 1, x + 1, y + 1), fill='black')

    def line_make(self, event):
        print(event)
        print(self.prev1)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.create_line((x - 1, y - 1, x + 1, y + 1), fill='black')
        self.line = self.canvas.create_line(self.prev1.x, self.prev1.y, event.x, event.y)
        self.canvas.unbind('<B1-ButtonRelease>')
        self.rect_color = (messagebox.askyesno(title='Color', message='Want to color the line?'))
        if (self.rect_color == True):
            self.color()
            self.canvas.itemconfigure(self.line, fill=str(self.chosen_color[1]))

    def click_line(self):
        messagebox.showinfo(title="Mark the line", message='Mark two points on the canvas to make the line')
        self.canvas.bind('<B1-ButtonRelease>', self.mouse_rel_line)

    def mouse_rel_line(self,event):
         self.prev1 = event
         self.canvas.bind('<B1-ButtonRelease>', self.line_make)
         x = self.canvas.canvasx(event.x)
         y = self.canvas.canvasy(event.y)
         self.canvas.create_line((x - 1, y - 1, x + 1, y + 1), fill='black')

    def delete(self):
        self.entry_name = ttk.Entry(self.frame1, width=12, font=('Arial', 10))
        self.entry_name.grid(row=6, column=0, padx=5)
        ttk.Button(self.frame1, text = 'Submit',
                   command = self.submit).grid(row = 7, column = 0, padx = 5, pady = 5, sticky = 'e')


    def submit(self):
        print('Name:{}'.format(self.entry_name.get()))
        if self.entry_name.get()=="rectangle":
            self.canvas.delete(self.rect)
        if self.entry_name.get()=="oval":
            self.canvas.delete(self.oval)
        if self.entry_name.get()=="line":
            self.canvas.delete(self.line)
        elif self.entry_name.get()=="all":self.canvas.delete("all")

def main():
    root=Tk()
    painting=Paint(root)

    root.mainloop()

if __name__=="__main__": main()

