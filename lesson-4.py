# pogram-4: creating input box

from tkinter import*
root=Tk()
e= Entry(root,fg="white",bg="black")
e.pack()
e.insert(0,"ENTER YOUR NAME")

def myClick():
    myLabel=Label(root,text="I am clicked")
    myLabel.pack()
    
# myBtn=Button(root,text="Click Me", padx=50,pady=10)
myBtn=Button(root,text="Click Me", padx=50,pady=10,command=myClick,fg="white",bg="black")
myBtn.pack()

root.mainloop()