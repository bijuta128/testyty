from tkinter import *
import pickle
def register_user():
   username_info=username.get()
   password_info=password.get()

   file=open(username_info+"b.txt","w")
   file.write(username_info+"\n")
   file.write(password_info+"\n")
   file.close()



def register():
    wn.destroy()
    global wn1
    wn1=Tk()
    wn1.title("jgshjkf")
    wn1.geometry("400x400")
    Label(wn1,text="welcome to register session").place(x=5,y=10)
    global username
    global username_entry
    global password
    global password_entry

    username=StringVar()
    password=StringVar()

    Label(wn1,text="Username").place(x=80,y=80)
    username_entry=Entry(wn1,textvariable=username)
    username_entry.place(x=160,y=80)
    Label(wn1,text="Password").place(x=80,y=140)
    password_entry=Entry(wn1,textvariable=password)
    password_entry.place(x=160,y=140)
    Button(wn1,text="Register",width=30,height=2,command=register_user).place(x=100,y=190)


def main():
    global wn
    wn=Tk()
    wn.title("xuchi")
    wn.geometry("300x300")
    Label(wn,text="gfjkashodfyhkjwhkjdf",width="30",height="2").place(x=10,y=12)
    Button(wn,text="Login",width="30",height="2").place(x=50,y=80)
    Button(wn,text="register",command=register).place(x=50,y=140)
    wn.mainloop()
main()