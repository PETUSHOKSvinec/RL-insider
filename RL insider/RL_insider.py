from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import fileinput
from tkinter.messagebox import *


#sp=["zomba","fsl"]

root=Tk()
root.geometry("500x500")
root.title("Elemendid Tkinteris")

def funktion(a):
    tabs.select(a)

tabs=ttk.Notebook(root)

texts=["Boost","Trail","Wheels","Neljas","Viies","Kuues","Seitsmes","Kaheksas"]
#def update(name,i):
	#tabs.select(i)
	#index.append(btn)
	#print(btn)



def images(name,i):
	global img
	tabs.select(i)
	img=PhotoImage(file=name).subsample(4)
	can1.create_image(10,10,image=img,anchor=NW)
	can2.create_image(10,10,image=img,anchor=NW)
	can3.create_image(10,10,image=img,anchor=NW)
	can4.create_image(10,10,image=img,anchor=NW)
	can5.create_image(10,10,image=img,anchor=NW)
	can6.create_image(10,10,image=img,anchor=NW)

tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tab5=Frame(tabs)
tab6=Frame(tabs)
tabs.add(tab1,text="Decal")
tabs.add(tab2,text="Boost")
tabs.add(tab4,text="Boody")
tabs.add(tab5,text="Wheels")
tabs.add(tab6,text="Goal Explosions")
tabs.pack()
can1=Canvas(tab1,width=500,height=300)
can1.pack()
can2=Canvas(tab2,width=500,height=300)
can2.pack()
can3=Canvas(tab3,width=500,height=300)
can3.pack()
can4=Canvas(tab4,width=500,height=300)
can4.pack()
can5=Canvas(tab5,width=500,height=300)
can5.pack()
can6=Canvas(tab6,width=500,height=300)
can6.pack()
M=Menu(root)
root.config(menu=M)

#sp=["zomba","fsl"]






#zomba=lambda:images("zombax.png",4))

m2=Menu(M,tearoff=0)
M.add_cascade(label="colors",menu=m2)
m2.add_command(label="Default", command=lambda:root.config(bg="Gray"))
m2.add_command(label="Purple", command=lambda:root.config(bg="violet"))
m2.add_command(label="Crimson",command=lambda:root.config(bg="red"))
m2.add_command(label="Light Blue",command=lambda:root.config(bg="aqua"))
m2.add_command(label="Forest green",command=lambda:root.config(bg="green"))
m2.add_command(label="Lime",command=lambda:root.config(bg="lime"))
m2.add_command(label="Yellow",command=lambda:root.config(bg="yellow"))
m2.add_command(label="Orange",command=lambda:root.config(bg="#FFA500"))
m2.add_command(label="Titanium White ",command=lambda:root.config(bg="white"))
m2.add_command(label="Grey",command=lambda:root.config(bg="#DCDCDC"))


m3=Menu(M,tearoff=0)
M.add_cascade(label="Items",menu=m3)
m3.add_command(label="Common", command=lambda:images("dieci.png",3))

m3.add_command(label="Rare",command=lambda:images("octanedrag.png",0))

m3.add_command(label="Very rare",command=lambda:images("burnout.png",1))

m3.add_command(label="Import",command=lambda:images("dominustw.png",2))

m3.add_command(label="Exotic",command=lambda:images("zombax.png",3))

m3.add_command(label="Black Market",command=lambda:images("dueling_drag.png",4))


#m4=Menu(M,tearoff=1)
#m4.add_command(label="Tab2",command=lambda:images("dieci.png",0))
#m4.add_command(label="Tab1",command=lambda:cq(1))


tabs.pack(fill="both")
root.mainloop()
