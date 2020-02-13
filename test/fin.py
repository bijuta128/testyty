from tkinter import*
wn=Tk()

wn.title("fin_form")
wn.geometry("600x400")
lbl_1=Label(wn,text="hello i am bijuta ,i am from thankot." )
lbl_2=Label(wn,text="hello world")
lbl_1.pack(padx=20, pady=20)
lbl_2.pack(padx=10, pady=10)
btn_1=Button(wn,text="click")
btn_1.pack(side='left')
#btn_1.bind("<Button_1 >",)
wn.mainloop()
