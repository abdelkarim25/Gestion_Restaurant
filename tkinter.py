import tkinter as tk
from cProfile import label
from tkinter import Entry, Button
from tkinter.ttk import PanedWindow

window = tk.Tk()

window.geometry("700x500")
def calculate():
    Pizza=e1.get()
    if not Pizza:
        Pizza=0
    Tacos=e2.get()
    if not Tacos:
        Tacos=0
    Sandwich=e3.get()
    if not Sandwich:
        Sandwich=0
    Burger=e4.get()
    if not Burger:
        Burger=0
    Frites=e5.get()
    if not Frites:
        Frites=0
    Nuggets=e6.get()
    if not Nuggets:
        Nuggets=0
    Soda=e7.get()
    if not Soda:
        Soda=0
    Limonade=e8.get()
    if not Limonade:
        Limonade=0
    print(type(Limonade))
    total=((int(Pizza)*40)+(int(Tacos)*49)+(int(Sandwich)*30)+(int(Burger)*32)+(int(Frites)*15)+(int(Nuggets)*35)+(int(Soda)*15)+(int(Limonade)*15))
    label19 = tk.Label(window,text=total,font="times 18")
    label19.place(x=150, y=410)
    label19 = tk.Label(window, text="dh", font="times 18")
    label19.place(x=210, y=410)

label0 = tk.Label(window, text="Bienvenue au restaurant", font="times 30 bold")
label0.place(x=350,y=20,anchor="center")




label1 = tk.Label(window, text="Menu", font="times 28 bold")
label1.place(x=550,y=40)

label1 = tk.Label(window, text="Pizza             40dh", font="times 18")
label1.place(x=500, y=80)

label2 = tk.Label(window, text="Tacos            49dh", font="times 18")
label2.place(x=500, y=120)

label3 = tk.Label(window, text="Sandwich      30dh", font="times 18")
label3.place(x=500, y=160)

label4 = tk.Label(window, text="Burger          32dh", font="times 18")
label4.place(x=500, y=200)

label5 = tk.Label(window, text="Frites            15dh", font="times 18")
label5.place(x=500, y=240)

label6 = tk.Label(window, text="Nuggets        35dh", font="times 18")
label6.place(x=500, y=280)

label7 = tk.Label(window, text="Soda             15dh", font="times 18")
label7.place(x=500, y=340)

label8 = tk.Label(window, text="Limonade    15dh", font="times 18")
label8.place(x=500, y=380)





label9 = tk.Label(window, text="Choisissez une commande", font="times 20 bold")
label9.place(x=70,y=70)

label10 = tk.Label(window, text="Pizza", font="times 18")
label10.place(x=20, y=120)
e1=Entry(window)
e1.place(x=20,y=150)

label11 = tk.Label(window, text="Tacos", font="times 18")
label11.place(x=20, y=170)
e2=Entry(window)
e2.place(x=20,y=200)

label12 = tk.Label(window, text="Sandwich", font="times 18")
label12.place(x=300, y=120)
e3=Entry(window)
e3.place(x=300,y=150)

label13 = tk.Label(window, text="Burger", font="times 18")
label13.place(x=20, y=220)
e4=Entry(window)
e4.place(x=20,y=250)

label14 = tk.Label(window, text="Frites", font="times 18")
label14.place(x=300, y=170)
e5=Entry(window)
e5.place(x=300,y=200)

label15 = tk.Label(window, text="Nuggets", font="times 18")
label15.place(x=300, y=220)
e6=Entry(window)
e6.place(x=300,y=250)

label16 = tk.Label(window, text="Soda", font="times 18")
label16.place(x=20, y=270)
e7=Entry(window)
e7.place(x=20,y=300)

label17 = tk.Label(window, text="Limonade", font="times 18")
label17.place(x=300, y=270)
e8=Entry(window)
e8.place(x=300,y=300)

b2=Button(window,text="bill",width=20,command=calculate)
b2.place(x=150,y=350)




window.mainloop()
