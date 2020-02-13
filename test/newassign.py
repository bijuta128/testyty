from tkinter import*
from tkinter import messagebox

bij=Tk()
bij.title("mero_form")
bij.geometry("900x700")
lbl_1=Label(bij,text="mero ragister form", fg='green', font='Ariel')
lbl_2=Label(bij,text="Name",fg='blue', bg='red')
lbl_1.pack(padx=20,pady=10)
lbl_2.pack(padx=20,pady=10)

ent0=Entry(fg="blue",bg="red" ,width=40 )
ent0.pack(padx=20, pady=10)
lbl3=Label(bij,text="choose your gender")
lbl3.pack(padx=20, pady=10)
rad0=Radiobutton(bij,text="Female",value=1)
rad1=Radiobutton(bij,text="male",value=2)
rad2=Radiobutton(bij,text="others", value=3)
rad0.pack(padx=20,pady=10)
rad1.pack(padx=20, pady=10)
rad2.pack(padx=20, pady=10)
lbl4=Label(bij,text="Email", bg="blue" ,fg="white")
lbl4.pack(padx=10, pady=20)
ent1=Entry(fg="voilet",bg="white")
ent1.pack(padx=20,pady=10)




btn_1=Button(bij,text="click")
btn_1.pack(side="left")
#btn_1.bind("<Button_1  > " ,abc())


bij.mainloop()



