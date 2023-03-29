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
        ent_p=ent_poisk.get()
        if ent_p in riik_peal:
            lbl_otvet.config(text=riik_peal[ent_p])
        elif ent_p in peal_riik:
            lbl_otvet.configure(text=peal_riik[ent_p])
        else:
            lbl_otvet.config(text="Ei leitud")
    riik_peal,peal_riik=sp("riigid_pealinnad.txt")
    aken_poisk=Tk()
    aken_poisk.title("Nimekirja")
    aken_poisk.iconbitmap("kot.ico")
    lbl_poisk=Label(aken_poisk,text="Leia pealinn riigi järgi ja vastupidi",font="Algerian 25",height=2)
    lbl_otvet=Label(aken_poisk,bg="lightgray",font="Arial 15",height=1,width=10)
    ent_poisk=Entry(aken_poisk, fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
    test=Button(aken_poisk,text="test",command=poisk2)
    lbl_poisk.pack()
    lbl_otvet.pack()
    ent_poisk.pack()
    test.pack()

def uus(event):
    global up,ur
    u=Toplevel()
    u.title("Uus")
    u.iconbitmap("kot.ico")
    lbl_poisk=Label(u,text="Lisage uus riik ja pealinn",font="Algerian 25",height=2)
    uus_riik=Label(u,text="Sisestage uus riik",font="Arial 20")
    uus_peal=Label(u,text="Sisestage uus pealinn",font="Arial 20")
    up=Entry(u,fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
    ur=Entry(u,fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
    salv=Button(u,text="Enter", font="Arial 15", relief=GROOVE)
    uus_p=up.get()
    uus_r=ur.get()
    spis1.update({uus_r:uus_p})

    salv.bind("<Button-1>",salvesta())
    lbl_poisk.pack()
    uus_riik.pack()
    ur.pack()
    uus_peal.pack() 
    up.pack()
    salv.pack()
    u.mainloop()
def salvesta():
        global up,ur
        uus_p=up.get()
        uus_r=ur.get()
        spis1.update({uus_r:uus_p})
        riik=list(spis1.keys())
        linn=list(spis1.values())
        y=[]
        riik.append(uus_r) 
        linn.append(uus_p) 
        for i in range (len(riik)):
            y.append(riik[i]+"-"+linn[i]+"\n")
        file=open("riigid_pealinnad.txt",'w', encoding="utf-8-sig")
        file.writelines(y)

sonastik={}
spis1,spis2=sp("riigid_pealinnad.txt")
aken=Tk()
aken.title("Euroopa riigid")
aken.geometry("450x350")
aken.iconbitmap("kot.ico")
lbl=Label(aken,text="Euroopa riigid",font="Algerian 25",height=2,width=15)
nimekirja_btn=Button(aken,text="Vaata nimekirja", font="Arial 15", relief=GROOVE)
poisk_btn=Button(aken,text="Leia pealinn riigi järgi ja vastupidi", font="Arial 15", relief=GROOVE)
lisa_btn=Button(aken,text="Lisage uus riik ja pealinn",font="Arial 15", relief=GROOVE)
parand_btn=Button(aken,text="Parandage riiki/pealinna",font="Arial 15", relief=GROOVE)
test_btn=Button(aken,text="Teadmiste kontroll",font="Arial 15", relief=GROOVE)

nimekirja_btn.bind("<Button-1>",vaata_nimekirja)
poisk_btn.bind("<Button-1>",poisk)
lisa_btn.bind("<Button-1>",uus)

lbl.pack()
nimekirja_btn.pack()
poisk_btn.pack()
lisa_btn.pack()
parand_btn.pack()


aken.mainloop()
