from tkinter import *
wn=Tk()
wn.title('userloginform')
wn.geometry('400x300+350+200')

labeluser=Label(wn,text='Username')
labeluser.grid(row=0,column=0)
entryuser=Entry(wn)
entryuser.grid(row=0,column=1)



labeluser=Label(wn,text='Password')
labeluser.grid(row=1,column=0)
entryuser=Entry(wn)
entryuser.grid(row=1,column=1)



def reg():
    wn1=Tk()

btnregister=Button(wn,text='Register',command=reg)
btnregister.grid(row=2,columnspan=2)






wn.mainloop()