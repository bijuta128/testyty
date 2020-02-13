from tkinter import*
from tkinter import messagebox
import pickle
def register():
    l= Label.get()
    l2= Label.get()
    l3= Label.get()
    l4= Label.get()
    lst=[l,l2,l3,l4]
    file=open ("assignmrnt.txt","rb+")
    pickle.dump(lst,file)
    file.close()
    messagebox.info("registration saved")
wn=Tk()




