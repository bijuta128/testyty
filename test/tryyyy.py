from tkinter import*
bj=Tk()
bj.geometry("400x400")
bj.title("employees registration form" )

l=Label(bj,text="for registration click here")
l1=Label(bj,text="for login click here")
b1=Button(bj,text="registration",command="reg")
b2=Button(bj,text="login",command="log")
l.grid(row=1,column=1)
b1.grid(row=2,column=1)
l1.grid(row=3,column=1)
b2.grid(row=4,column=1)
bj.mainloop()
global username
global password
global username_Entry
username=StringVar()
password=StringVar()