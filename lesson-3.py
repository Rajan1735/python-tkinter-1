# pogram-3: creating buttons
from tkinter import*
root=Tk()
def myClick():
    myLabel=Label(root,text="I am clicked")
    myLabel.pack()
    
# myBtn=Button(root,text="Click Me", padx=50,pady=10)
myBtn=Button(root,text="Click Me", padx=50,pady=10,command=myClick,fg="white",bg="black")
myBtn.pack()

root.mainloop()