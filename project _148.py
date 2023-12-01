from tkinter import *

import random

root = Tk()
root.title("List")
root.geometry("400x400")

label1 = Label(root)
label2 = Label(root)
list1 = ["Bottle", "Tiffin", "ID Card", "Chocolate", "Chips", "Tickets", "Handkerchief", "Mobiles"]
 

def randomlist():
    randomlist = random.sample(range(0, 3),1)
    label1["text"] = "Listed Item : " + str(list1)
    label2["text"] = "Put Item no. " + str(randomlist) + " In bag"
   
btn = Button(root, text = "Which Item to put in bag ?", command=randomlist,  bg = "orange", fg = "white")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label1.place(relx=0.5, rely=0.4, anchor=CENTER)
label2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()

