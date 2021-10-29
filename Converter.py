#Developer Name => Ashwini S Prabhu
#Institution Name => Presidency Univeristy, Bangalore,India

from tkinter import*

root = Tk()

root.title("CALCULATOR")

root.configure(bg='black')

root.state('zoomed')

root.label = Label(root,text='Developer - Ashwini S Prabhu',bg ="black",fg='yellow',font=('freemono bold',25))
root.label.place(x=600,y=700)

def a1():
    a1 = Toplevel()
    a1.title('Centimeter to Meter')
    a1.state('zoomed')
    a1.configure(bg='black')

    a1.label = Label(a1,text="Enter the number in Centimeter",font=10,bg ="black",fg='white')
    a1.label.place(x=605,y=53)
    ip1 = Entry(a1, width=20,font=10,borderwidth=2)
    ip1.place(x=625,y=110)

    def sin():
        ip11 = ip1.get()
        o1 = float(ip11)/100

        a1.label = Label(a1,text="In Meters:",font=10,bg ="black",fg='white')
        a1.label.place(x=680,y=260)

        a1.label = Label(a1,text=o1,font=10,bg ="black",fg='white')
        a1.label.place(x=775,y=260)

    a12 = Button(a1,text='Compute',command=sin,font=25)
    a12.place(x=700,y=175)

    def quit1():
        {
        a1.destroy()
        }
    a4 = Button(a1,text='Back to Main Menu',command=quit1,font=25)
    a4.place(x=1300,y=50)

    a1.label = Label(a1,text='Developer - Ashwini S Prabhu',bg ="black",fg='yellow',font=('freemono bold',25))
    a1.label.place(x=600,y=700)

def a2():
    a2 = Toplevel()
    a2.title('Centimeter to Inch')
    a2.state('zoomed')
    a2.configure(bg='black')

    a2.label = Label(a2,text="Enter the number in Centimeter",font=10,bg ="black",fg='white')
    a2.label.place(x=605,y=53)
    ip11 = Entry(a2, width=20,font=10,borderwidth=2)
    ip11.place(x=625,y=110)

    def cos():
        ip111 = ip11.get()
        o1 = float(ip111)*0.394

        a2.label = Label(a2,text="In Inches:",font=10,bg ="black",fg='white')
        a2.label.place(x=680,y=260)

        a2.label = Label(a2,text=o1,font=10,bg ="black",fg='white')
        a2.label.place(x=775,y=260)

    a12 = Button(a2,text='Compute',command=cos,font=25)
    a12.place(x=700,y=175)

    def quit2():
        {
        a2.destroy()
        }
    a4 = Button(a2,text='Back to Main Menu',command=quit2,font=25)
    a4.place(x=1300,y=50)

    a2.label = Label(a2,text='Developer - Ashwini S Prabhu',bg ="black",fg='yellow',font=('freemono bold',25))
    a2.label.place(x=600,y=700)

def a3():
    a3 = Toplevel()
    a3.title('Meter to Centimeter')
    a3.state('zoomed')
    a3.configure(bg='black')

    a3.label = Label(a3,text="Enter the number Meters",font=10,bg ="black",fg='white')
    a3.label.place(x=630,y=53)
    ip12 = Entry(a3, width=20,font=10,borderwidth=2)
    ip12.place(x=625,y=110)

    def tan():
        ip112 = ip12.get()
        o1 = float(ip112)*100

        a3.label = Label(a3,text="In Centimeter:",font=10,bg ="black",fg='white')
        a3.label.place(x=680,y=260)

        a3.label = Label(a3,text=o1,font=10,bg ="black",fg='white')
        a3.label.place(x=805,y=260)

    a13 = Button(a3,text='Compute',command=tan,font=25)
    a13.place(x=700,y=175)

    def quit3():
        {
        a3.destroy()
        }
    a4 = Button(a3,text='Back to Main Menu',command=quit3,font=25)
    a4.place(x=1300,y=50)

    a3.label = Label(a3,text='Developer - Ashwini S Prabhu',bg ="black",fg='yellow',font=('freemono bold',25))
    a3.label.place(x=600,y=700)

def a4():
    a4 = Toplevel()
    a4.title('Inch to Centimeter')
    a4.state('zoomed')
    a4.configure(bg='black')

    a4.label = Label(a4,text="Enter the number Inch",font=10,bg ="black",fg='white')
    a4.label.place(x=630,y=53)
    ip14 = Entry(a4, width=20,font=10,borderwidth=2)
    ip14.place(x=625,y=110)

    def cose():
        ip114 = ip14.get()
        o1 = float(ip114)*2.54

        a4.label = Label(a4,text="In Centimeter:",font=10,bg ="black",fg='white')
        a4.label.place(x=680,y=260)

        a4.label = Label(a4,text=o1,font=10,bg ="black",fg='white')
        a4.label.place(x=805,y=260)

    a14 = Button(a4,text='Compute',command=cose,font=25)
    a14.place(x=700,y=175)

    def quit4():
        {
        a4.destroy()
        }
    a22 = Button(a4,text='Back to Main Menu',command=quit4,font=25)
    a22.place(x=1300,y=50)

    a4.label = Label(a4,text='Developer - Ashwini S Prabhu',bg ="black",fg='yellow',font=('freemono bold',25))
    a4.label.place(x=600,y=700)

a = Button(root,text="Centimeter to Meter",command=a1,bg ="white",fg='black',borderwidth=15,font=100)
a.place(x=675,y=200)

b = Button(root,text="Centimeter to Inch",command=a2,bg ="white",fg='black',borderwidth=15,font=100)
b.place(x=675,y=300)

c = Button(root,text="Meter to Centimeter",command=a3,bg ="white",fg='black',borderwidth=15,font=100)
c.place(x=675,y=400)

d = Button(root,text="Inch to Centimeter",command=a4,bg ="white",fg='black',borderwidth=15,font=100)
d.place(x=675,y=500)

root.mainloop()

#-------------------------- © copyrights owned by Ashwini S Prabhu-------------#
