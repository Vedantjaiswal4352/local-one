from tkinter import *
from Accountdb import *
from tkinter.messagebox import *
import random as r
class openaccountbox(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.l1=Label(self,text="Name")
        self.nm=StringVar()
        self.bl=IntVar()
        self.dt=StringVar()
        self.phn=IntVar()
        self.adr=StringVar()
        self.l1.grid(row=1,column=0,padx=5,pady=5)
        self.t1=Entry(self,textvariable=self.nm)
        self.t1.grid(row=1,column=1,columnspan=2,padx=5,pady=5)

        self.l2=Label(self,text="Balance")
        self.l2.grid(row=2,column=0,padx=5,pady=5)
        self.t2=Entry(self,textvariable=self.bl)
        self.t2.grid(row=2,column=1,columnspan=2,padx=5,pady=5)

        self.l3=Label(self,text="DOB")
        self.l3.grid(row=3,column=0,padx=5,pady=5)
        self.t3=Entry(self,textvariable=self.dt)
        self.t3.grid(row=3,column=1,columnspan=2,padx=5,pady=5)

        self.l4=Label(self,text="PHONE")
        self.l4.grid(row=4,column=0,padx=5,pady=5)
        self.t4=Entry(self,textvariable=self.phn)
        self.t4.grid(row=4,column=1,columnspan=2,padx=5,pady=5)

        self.l5=Label(self,text="ADDRESS")
        self.l5.grid(row=5,column=0,padx=5,pady=5)
        self.t5=Entry(self,textvariable=self.adr)
        self.t5.grid(row=5,column=1,columnspan=2,padx=5,pady=5)

        self.b1=Button(self,text="Save",command=self.save)
        self.b1.grid(row=6,column=1,padx=5,pady=5)
        self.b2=Button(self,text="cancel")
        self.b2.grid(row=6,column=2,padx=5,pady=5)

    def save(self):
        name=self.nm.get()
        balance=self.bl.get()
        dte=self.dt.get()
        phn=self.phn.get()
        adr=self.adr.get()
        ac=r.randint(10000,99999)

        a=Account()
        accno=a.openAccount(name,balance,ac,dte,phn,adr)
        showinfo("Bank","Account Created...\n Accno: "+str(ac))

class Depositaccountbox(Toplevel):
    def __init__(self):
        super().__init__()
        self.acn=IntVar()
        self.amt=IntVar()
        self.l1=Label(self,text="Accno.")
        self.l1.grid(row=0,column=0,padx=5,pady=5)
        self.t1=Entry(self,textvariable=self.acn)
        self.t1.grid(row=0,column=1,columnspan=2,padx=5,pady=5)
        self.l2=Label(self,text="Amount")
        self.l2.grid(row=1,column=0,padx=5,pady=5)
        self.t2=Entry(self,textvariable=self.amt)
        self.t2.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        self.b1=Button(self,text="Deposit",command=self.save)
        self.b1.grid(row=2,column=1,padx=5,pady=5)
    def save(self):
        an=self.acn.get()
        am=self.amt.get()
        a=Account()
        if a.deposit(an,am):
            showinfo("BANK","Amount is Successfully Deposted...")
        else:
            showerror("BANK","Failed..")

class Withdrawaccountbox(Toplevel):
    def __init__(self):
        super().__init__()
        self.acn=IntVar()
        self.amt=IntVar()
        self.l1=Label(self,text="Accno.")
        self.l1.grid(row=0,column=0,padx=5,pady=5)
        self.t1=Entry(self,textvariable=self.acn)
        self.t1.grid(row=0,column=1,columnspan=2,padx=5,pady=5)
        self.l2=Label(self,text="Amount")
        self.l2.grid(row=1,column=0,padx=5,pady=5)
        self.t2=Entry(self,textvariable=self.amt)
        self.t2.grid(row=1,column=1,columnspan=2,padx=5,pady=5)
        self.b1=Button(self,text="Withdraw",command=self.save)
        self.b1.grid(row=2,column=1,padx=5,pady=5)
    def save(self):
        an=self.acn.get()
        am=self.amt.get()
        a=Account()
        if a.withdraw(an,am):
            showinfo("BANK","Amount is Withdraw")
        else:
            showerror("BANK","insuficient Balance")

class searchaccountbox(Toplevel):
    def __init__(self):
        super().__init__()
        self.acn=IntVar()
        self.l1=Label(self,text="Accno.")
        self.l1.grid(row=0,column=0,padx=5,pady=5)
        self.t1=Entry(self,textvariable=self.acn)
        self.t1.grid(row=0,column=1,columnspan=2,padx=5,pady=5)
        self.b1=Button(self,text="Search",command=self.save)
        self.b1.grid(row=1,column=1,padx=5,pady=5)

    def save(self):
        an=self.acn.get()
        a=Account()
        res=a.search(an)
        if res!=None:
            msg="MANE : "+str(res[0])+"\nACNO : "+str(res[1])+"\nDOB : "+str(res[2])+"\nPHONE : "+str(res[3])+"\nADDRESS : "+str(res[4])+"\nBalance : "+str(res[5])
            showinfo("BANK",msg)
        else:
            showerror("BANK","ACCOUNT NOT FOUND")

class listAccounts(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("350x400")
        self.txt=Text(self)
        self.txt.pack()
        a=Account()
        res=a.listAccount()
        for lst in res:
            an=str(lst[0])
            nm=str(lst[1])
            bl=str(lst[5])
            self.txt.insert(1.0,"| "+an+"\t| "+nm+"\t\t| "+bl+"\t  |\n")
        self.txt.insert(1.0, "| Name\t| Acno\t\t| Balance\t|\n")


class mainframe(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.b1=Button(self,text="Open Account",width=200,bg="skyblue",fg="white",font="arial 20 bold",command=self.funopenaccount)
        self.b1.pack(padx=5,pady=5)
        self.b2=Button(self,text="Deposit",width=200,bg="skyblue",fg="white",font="arial 20 bold",command=self.fundepositaccount)
        self.b2.pack(padx=5,pady=5)
        self.b3=Button(self,text="Withdraw",width=200,bg="skyblue",fg="white",font="arial 20 bold",command=self.funwithdrawaccount)
        self.b3.pack(padx=5,pady=5)
        self.b4=Button(self,text="Search",width=200,bg="skyblue",fg="white",font="arial 20 bold",command=self.funsearchaccount)
        self.b4.pack(padx=5,pady=5)
        self.b5=Button(self,text="List",width=200,bg="skyblue",fg="white",font="arial 20 bold",command=self.funlistaccounts)
        self.b5.pack(padx=5,pady=5)

    def funopenaccount(self):
        box=openaccountbox()
        box.mainloop()

    def funlistaccounts(self):
        box=listAccounts()
        box.mainloop()

    def fundepositaccount(self):
        box=Depositaccountbox()
        box.mainloop()

    def funwithdrawaccount(self):
        box=Withdrawaccountbox()
        box.mainloop()

    def funsearchaccount(self):
        box=searchaccountbox()
        box.mainloop()
main=mainframe()
main.mainloop()