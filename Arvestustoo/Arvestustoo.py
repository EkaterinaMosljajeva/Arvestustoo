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
            lbl_otvet.config(text=peal_riik[ent_p])
        else:
            lbl_otvet.config(text="Ei leitud")
    riik_peal,peal_riik=sp("riigid_pealinnad.txt")
    aken_poisk=Tk()
    aken_poisk.title("Nimekirja")
    aken_poisk.iconbitmap("kot.ico")
    lbl_poisk=Label(aken_poisk,text="Leia pealinn riigi järgi ja vastupidi",font="Algerian 25",height=2)
    lbl_otvet=Label(aken_poisk,font="Arial 20",height=1,width=10)
    ent_poisk=Entry(aken_poisk, fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
    but_poisk=Button(aken_poisk,text="Enter",command=poisk2,font="Arial 20")
    lbl_poisk.pack()
    lbl_otvet.pack()
    ent_poisk.pack()
    but_poisk.pack()
def salvesta(spis1):
        global up,ur
        uus_p=up.get()        
        uus_r=ur.get()
        spis1.update({uus_r:uus_p})
        riik=list(spis1.keys())
        linn=list(spis1.values())
        print(riik)
        y=[]
        riik.append(uus_r) 
        linn.append(uus_p)
        for i in range (len(riik)-1):
            y.append(riik[i]+"-"+linn[i]+"\n")
        file=open("riigid_pealinnad.txt",'w', encoding="utf-8-sig")
        file.writelines(y)
def uus():
    spis1,spis2=sp("riigid_pealinnad.txt")
    global up,ur
    u=Toplevel()
    u.title("Uus")
    u.iconbitmap("kot.ico")
    lbl_poisk=Label(u,text="Lisage uus riik ja pealinn",font="Algerian 25",height=2)
    uus_riik=Label(u,text="Sisestage uus riik",font="Arial 20")
    uus_peal=Label(u,text="Sisestage uus pealinn",font="Arial 20")
    up=Entry(u,fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
    ur=Entry(u,fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
    salv=Button(u,text="Enter", font="Arial 15", relief=GROOVE,command=lambda:salvesta(spis1))


    lbl_poisk.pack()
    uus_riik.pack()
    ur.pack()
    uus_peal.pack() 
    up.pack()
    salv.pack()
    u.mainloop()


#def igra(event):
#    def proverka(event):
#        o=1
#        if o==1:
#                rand=choice(riik)
#                ind=riik.index(rand)
#                vopr.config(igr,text=linn[ind])
#                sona=ent_igta.get()
#                if sona.title in riik[ind]:
#                    otv_igr.config(igr,text="Õige")
#                    ko+=1
#                    n+=1
#                else:
#                    otv_igr.config(igr,text="Vale")
#                    n+=1
#        elif o==2:
#                rand=choice(linn)
#                ind=linn.index(rand)
#                vopr.config(igr,text=linn[ind])
#                sona=ent_igta.get()
#                if sona in linn[ind]:
#                    otv_igr.config(igr,text="Õige")
#                    n+=1
#                    ko+=1
#                else:
#                    otv_igr.config(igr,text="Vale")
#                    n+=1
#        print(f"{round(ko/n*100,1)}% vastused on õige ja {round(100-ko/n*100,1)}% on vale")
#    ko=0
#    riik=list(spis1.keys())
#    linn=list(spis1.values())
#    igr=Toplevel()
#    igr.title("Mäng")
#    igr.iconbitmap("kot.ico")
#    lbl_igra=Label(igr,text="Teadmiste kontroll",font="Algerian 25",height=2,width=15)
#    vopr=Label(igr,bg="lightgray",font="Arial 15",height=1,width=10)
#    ent_igta=Entry(igr,fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
#    otv_igr=Label(igr, font="Arial 15", width=10)
#    prov=Button(igr,bg="red",width=15)

#    prov.bind("<Button-1>",proverka)

#    rand=choice(riik)
#    ind=riik.index(rand)
#    vopr.config(igr,text=linn[ind])

#    lbl_igra.pack()
#    vopr.pack()
#    ent_igta.pack()
#    otv_igr.pack()
#    prov.pack()

#    igr.mainloop() 
        #o=int(input("Kas arvame pealinnad(1) või riigid(2)?"))
 

sonastik={}
spis1,spis2=sp("riigid_pealinnad.txt")
aken=Tk()
aken.title("Euroopa riigid")
aken.geometry("450x350")
aken.iconbitmap("kot.ico")
lbl=Label(aken,text="Euroopa riigid",font="Algerian 25",height=2,width=15)
nimekirja_btn=Button(aken,text="Vaata nimekirja", font="Arial 15", relief=GROOVE)
poisk_btn=Button(aken,text="Leia pealinn riigi järgi ja vastupidi", font="Arial 15", relief=GROOVE)
lisa_btn=Button(aken,text="Lisage uus riik ja pealinn",font="Arial 15", relief=GROOVE,command=uus)
#test_btn=Button(aken,text="Teadmiste kontroll",font="Arial 15", relief=GROOVE)

nimekirja_btn.bind("<Button-1>",vaata_nimekirja)
poisk_btn.bind("<Button-1>",poisk)
#test_btn.bind("<Button-1>",igra)

lbl.pack()
nimekirja_btn.pack()
poisk_btn.pack()
lisa_btn.pack()
#test_btn.pack()


aken.mainloop()
