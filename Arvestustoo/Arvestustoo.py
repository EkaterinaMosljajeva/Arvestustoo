from tkinter import *
from random import *

riik_peal={}
tekst=""
def sp(f):
    peal_riik={}
    file=open(f,'r', encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split("-")
        riik_peal[k]=v
        peal_riik[v]=k
    return riik_peal,peal_riik

def vaata_nimekirja(event):
    global riik_peal,tekst
    nimekirja=Toplevel()
    nimekirja.title("Nimekirja")
    aken.iconbitmap("kot.ico")
    for key,value in riik_peal.items():
        tekst+=key+"-"+value+"\n"
    nimekirja_lbl=Label(nimekirja,text=tekst)
    nimekirja_lbl.pack()
    nimekirja.mainloop()

def poisk(event):
    def poisk2():
        h=str(ent_poisk.get())
        val=var.get()
        if val==1:
            lbl_otvet.configure(aken_poisk,text=riik_peal[h])
        elif val==2:
            lbl_otvet.configure(aken_poisk,text="kasd")
        else:
            pass

    riik_peal,peal_riik=sp("riigid_pealinnad.txt")
    aken_poisk=Tk()
    aken_poisk.title("Nimekirja")
    aken_poisk.iconbitmap("kot.ico")
    var=IntVar()
    lbl_poisk=Label(aken_poisk,text="Leia pealinn riigi järgi ja vastupidi",bg="lightgray",font="Algerian 25",height=2,width=15)
    check_riik=Radiobutton(aken_poisk, text="Riik pealinna järgi",font="Arial 20",variable=var,value=1)
    check_peal=Radiobutton(aken_poisk, text="Pealinn riiki järgi",font="Arial 20",variable=var,value=2)
    lbl_otvet=Label(aken_poisk,bg="lightgray",font="Algerian 25",height=1,width=5)
    ent_poisk=Entry(aken_poisk, fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
    test=Button(aken_poisk,text="test",command=poisk2)
    check_riik.deselect()
    check_peal.deselect()
    lbl_poisk.pack()
    lbl_otvet.pack()
    ent_poisk.pack()
    check_riik.pack()
    check_peal.pack()
    test.pack()
    #cr=check_riik.get()
    #if cr=="Riik":
    #try:
    #    if p==1:
    #        o=input("Sisestage riik: ")
    #        print(riik_peal[o])
    #    elif p==2:
    #        o=input("Sisestage pealinn: ")
    #        print(peal_riik[o])
    #except:
    #    uus("riigid_pealinnad.txt")

#def uus():
#    r=input("Kirjutage riigi: ")
#    while r in spis1:
#        r=input("See riik on ")
#    p=input("Kirjutage pealinn: ") 
#    while p in spis2:
#        p=input("See pealinn on ")
#    spis1.update({r:p}) 
#    salvesta()

def salvesta():
    riik=list(spis1.keys())
    linn=list(spis1.values())
    y=[]
    for i in range(len(spis1)):
        y.append(riik[i]+"-"+linn[i]+"\n")
    file=open("riigid_pealinnad.txt",'w', encoding="utf-8-sig")
    file.writelines(y)

sonastik={}
spis1,spis2=sp("riigid_pealinnad.txt")
aken=Tk()
aken.title("Euroopa riigid")
aken.geometry("450x350")
aken.iconbitmap("kot.ico")
lbl=Label(aken,text="Euroopa riigid",bg="lightgray",font="Algerian 25",height=2,width=15)
nimekirja_btn=Button(aken,text="Vaata nimekirja", font="Arial 15", relief=GROOVE)
poisk_btn=Button(aken,text="Leia pealinn riigi järgi ja vastupidi", font="Arial 15", relief=GROOVE)
lisa_btn=Button(aken,text="Lisage uus riik ja pealinn",font="Arial 15", relief=GROOVE)
parand_btn=Button(aken,text="Parandage riiki/pealinna",font="Arial 15", relief=GROOVE)
test_btn=Button(aken,text="Teadmiste kontroll",font="Arial 15", relief=GROOVE)

nimekirja_btn.bind("<Button-1>",vaata_nimekirja)
#poisk_btn.bind("<Button-1>",poisk)
lbl.pack()
nimekirja_btn.pack()
poisk_btn.pack()
lisa_btn.pack()
parand_btn.pack()


aken.mainloop()
