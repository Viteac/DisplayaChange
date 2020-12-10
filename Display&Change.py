from tkinter import *

canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

img = PhotoImage(file="pic1.gif")
canvas.create_image(20,20, anchor=NW, image=img)

def change_img():
    canvas.delete("all")
    canvas.img = PhotoImage(file="pic2.gif")
    canvas.create_image(20,20, anchor=NW, image=canvas.img)

master.after(3000, change_img) # run the change_img function in 3,000 milliseconds

mainloop()
