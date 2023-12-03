import tkinter
from tkinter import*
import function_for_gui
root=Tk()
root.title("Welcome to Daniele's video resolution changer GUI,enjoy!")

root.geometry('800x400')

Label(root, text='1 Change resolution to 360x240').grid(row=1)
Label(root, text='2 Change resolution to 160x120').grid(row=2)
Label(root, text='3 Change resolution to 1080x720').grid(row=3)
Label(root, text='4 Change resolution to 640x480').grid(row=4)
e1= Button(root, text="click for 1", command=function_for_gui.change_res('big_buck_bunny.mp4', 360,240)).grid(row=1, column=1)
e2= Button(root, text="click for 2", command=function_for_gui.change_res('big_buck_bunny.mp4',  160,120)).grid(row=2, column=1)
e3= Button(root, text="click for 3", command=function_for_gui.change_res('big_buck_bunny.mp4',  1080,720)).grid(row=3, column=1)
e4= Button(root, text="click for 4", command=function_for_gui.change_res('big_buck_bunny.mp4',  640,480)).grid(row=4, column=1)
btn = Button(root, text = 'Click me to exit!', bd = '5',command = root.destroy).grid(row=5, column=1)
root.mainloop()