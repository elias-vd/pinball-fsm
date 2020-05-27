from tkinter import *


def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


def create_circle(x, y, r, canvasName): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)






def main():

    root = Tk()

    myCanvas = Canvas()
    myCanvas.pack()
    cr1 = myCanvas.create_oval(100, 100, 200, 200)
    make_draggable(cr1)
    


    root.geometry("1000x660+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
