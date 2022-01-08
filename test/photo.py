from tkinter import *

root = Tk()
root.title("khjoo test")
# root.geometry("640x480+300+100")
root.geometry("640x480")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=10, text="버튼3")
btn3.pack()


root.resizable(True, False)

root.mainloop()
