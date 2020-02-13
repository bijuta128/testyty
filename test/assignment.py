from tkinter import *
from tkinter import messagebox

def log():

    wn=Tk()
    wn.geometry("600x400")
    lbl=Label(wn,text ="username")
    lbl.grid(row=0,column=0)
    lbl1=Label(wn,text="password")
    lbl1.grid(row=0,column=1)
    e1=Entry(wn,text="username")
    e1.grid(row=1,column=0)
    e2 =Entry(wn,text="password")
    e2.grid(row=1,column=1)
    button2=Button(wn,text="submit",command=log)
    button2.grid(row=4,columnspan=1)
    wn.mainloop()
def reg():
    global mainscreen
    global name
    global name_e
    global Address
    global _Number
    global mail
    global Namee
    global pw
    global con_pw
    name=StringVar()
    Address=StringVar()
    _Number=StringVar()
    mail=StringVar()
    Namee=StringVar()
    pw=StringVar()
    con_pw=StringVar()
    mainscreen.geometry("500x500")
    l=Label(mainscreen,text="Name",bg="white",fg="black")
    l2=Label(mainscreen,text="Address",bg="white",fg="black")
    l3=Label(mainscreen,text="Phone number",bg="white",fg="black")
    l4=Label(mainscreen,text="Email address",bg="white",fg="black")
    l5=Label(mainscreen,text="Username",bg="white",fg="black")
    l6=Label(mainscreen,text="Password",bg="white",fg="black")
    l7=Label(mainscreen,text="confirm password",bg="white",fg="black"
    l.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    l3.grid(row=2,column=0)
    l4.grid(row=3,column=0)
    l5.grid(row=4,column=0)
    l6.grid(row=5,column=0)
    l7.grid(row=6,column=0)
    name_e=Entry(mainscreen,textvariable=name)
    e2=Entry(mainscreen,textvariable=Address)
    e3=Entry(mainscreen,textvariable=_Number)
    e4=Entry(mainscreen,textvariable=mail)
    e5=Entry(w,textvariable=Namee)
    e6=Entry(wn,textvariable=pw)
    e7=Entry(wn,textvariable=con_pw)
    e.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2,column=1)
    e4.grid(row=3,column=1)
    e5.grid(row=4,column=1)
    e6.grid(row=5,column=1)
    e7.grid(row=6,column=1)
    button=Button(wn,text="submit")
    button.grid(row=7,columnspan=3)
def regis():
    name_info=_Name.get()
    add_info=Address.get()
    num_info=_Number.get()
    mail_info=mail.get()
    nam_info=Namee.get()
    p_info=pw.get()
    con_info=con_pw.get()

    user_store={"Name":[name_info],
              "Address":[add_info],
              "Phone number":[num_info],
              "Email address":[mail_info],
              "Username":[nam_info],
              "password":[p_info],
              "confirm password":[con_info]
                }
    e.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)

def main_screen():
    wn=Tk()
    wn.geometry("400x400")
    wn.title("employees registration form")
    l=Label(wn,text="for registration click here")
    l1=Label(wn,text="for login click here")
    b1=Button(wn,text="registration",command=reg)
    b2=Button(wn,text="login",command=log)
    l.grid(row=1,column=1)
    b1.grid(row=2,column=1)
    l1.grid(row=3,column=1)
    b2.grid(row=4,column=1)
    wn.mainloop()
main_screen()