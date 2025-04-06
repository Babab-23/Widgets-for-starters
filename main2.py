from tkinter import *
from datetime import date
root=Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")
Ibl=Label(text="Hey There!",fg="White",bg="blue",height=1,width=300)
name_Ibl=Label(text="Full Name",bg="red")
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="Welcome to Application! \nToday's date is: "
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.inset(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="Begin",command=display,height=1,bg="orange",fg="black")
Ibl.pack()
name_Ibl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()