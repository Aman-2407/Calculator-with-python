import tkinter
from tkinter import *
from tkinter import messagebox

val=""
A=0
operator=""
def btn_1isclicked():
    global val
    val=val+"1"
    data.set(val)

def btn_2isclicked():
    global val
    val=val+"2"
    data.set(val)

def btn_3isclicked():
    global val
    val=val+"3"
    data.set(val)

def btn_4isclicked():
    global val
    val=val+"4"
    data.set(val)

def btn_5isclicked():
    global val
    val=val+"5"
    data.set(val)

def btn_6isclicked():
    global val
    val=val+"6"
    data.set(val)

def btn_7isclicked():
    global val
    val=val+"7"
    data.set(val)

def btn_8isclicked():
    global val
    val=val+"8"
    data.set(val)

def btn_9isclicked():
    global val
    val=val+"9"
    data.set(val)

def btn_0isclicked():
    global val
    val=val+"0"
    data.set(val)

def btn_plusisclicked():
    global A
    global operator
    global val
    A=int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minusisclicked():
    global A
    global operator
    global val
    A=int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_multiplyisclicked():
    global A
    global operator
    global val
    A=int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_divideisclicked():
    global A
    global operator
    global val
    A=int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def clear_btnclicked():
    global A
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 =val
    if operator=="+":
        x=int((val2.split("+")[1]))
        c=A+x
        data.set(c)
        val=str(c)
    elif operator=="-":
        x=int((val2.split("-")[1]))
        c=A-x
        data.set(c)
        val=str(c)
    elif operator=="*":
        x=int((val2.split("*")[1]))
        c=A*x
        data.set(c)
        val=str(c)
    elif operator=="/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Division by 0 not possible ")
            A=""
            val=""
            data.set(val)
        else:
            c=int(A/x)
            data.set(c)
            val=str(c)
        

root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")
data=StringVar()
lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#fff",
    fg="#000",
)
lbl.pack(expand=True,fill="both",)
btnr1=Frame(root,bg="#000")
btnr1.pack(expand =True, fill="both",)

btnr2=Frame(root)
btnr2.pack(expand =True, fill="both",)

btnr3=Frame(root)
btnr3.pack(expand =True, fill="both",)

btnr4=Frame(root)
btnr4.pack(expand =True, fill="both",)

btn1=Button(
    btnr1,
    text="1",
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_1isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2=Button(
    btnr1,
    text="2",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
    command=btn_2isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)

btn3=Button(
    btnr1,
    text="3",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_3isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4=Button(
    btnr1,
    text="+",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
    command=btn_plusisclicked,
    
)
btn4.pack(side=LEFT, expand=True, fill="both",)





btn1=Button(
    btnr2,
    text="4",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_4isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2=Button(
    btnr2,
    text="5",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_5isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)

btn3=Button(
    btnr2,
    text="6",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_6isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4=Button(
    btnr2,
    text="-",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
    command=btn_minusisclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)




btn1=Button(
    btnr3,
    text="7",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_7isclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2=Button(
    btnr3,
    text="8",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_8isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)

btn3=Button(
    btnr3,
    text="9",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_9isclicked,
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4=Button(
    btnr3,
    text="*",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
    command=btn_multiplyisclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)




btn1=Button(
    btnr4,
    text="C",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
    command=clear_btnclicked,
)
btn1.pack(side=LEFT, expand=True, fill="both",)

btn2=Button(
    btnr4,
    text="0",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
     command=btn_0isclicked,
)
btn2.pack(side=LEFT, expand=True, fill="both",)

btn3=Button(
    btnr4,
    text="=",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
    command=result,
)
btn3.pack(side=LEFT, expand=True, fill="both",)

btn4=Button(
    btnr4,
    text="/",
    font=("Verdana",22),
     relief=GROOVE,
    border=0,
    command=btn_divideisclicked,
)
btn4.pack(side=LEFT, expand=True, fill="both",)


root.mainloop()