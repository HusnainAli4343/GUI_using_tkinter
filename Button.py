# importing module
from tkinter import *
# TK() is making window
root = Tk()
# title() is using for change the window title
root.title("GUI")
# geometry is use to change the window size and using "X" between the x-axis and y-axis
root.geometry("300x300")
# using Button() function to make button
# 1st of all we can use Button(where do you want to located the Button, text="Button Name",
# background_colour is denoted by bg="colour name", foreground colour is denoted by fg="colour name")
button_1 = Button(root, text="Hello", bg="Pink", fg="White")
# then pack() the button
button_1.pack()
# mainloop() is using display the window
root.mainloop()