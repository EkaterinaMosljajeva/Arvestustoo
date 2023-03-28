from tkinter import *
from random import *
def spisok(f):
    riik_peal={}
    peal_riik={}
    file=open(f,'r', encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split("-")
        riik_peal[k]=v
        peal_riik[v]=k
    return riik_peal,peal_riik

#def vaata_nimekirja(event):
#    nimekirja=Toplevel()
#    nimekirja.title("Nimekirja")
#    aken.iconbitmap("kot.ico")
#    nimekirja_lbl=Label(nimekirja,text=spis1,width=20)
#    nimekirja_lbl.pack()
#    nimekirja.mainloop()

sonastik={}
spis1,spis2=spisok("riigid_pealinnad.txt")
aken=Tk()
aken.title("Euroopa riigid")
aken.geometry("450x350")
aken.iconbitmap("kot.ico")
lbl=Label(aken,text="Euroopa riigid",bg="lightgray",font="Algerian 25",height=2,width=15)
nimekirja_btn=Button(aken,text="Vaata nimekirja", font="Arial 15", relief=GROOVE)
poisk_btn=Button(aken,text="Leia pealinn riigi järgi ja vastupidi", font="Arial 15", relief=GROOVE)

#nimekirja_btn.bind("<Button-1>",vaata_nimekirja)
poisk_btn
lbl.pack()
nimekirja_btn.pack()
poisk_btn.pack()
aken.mainloop()
