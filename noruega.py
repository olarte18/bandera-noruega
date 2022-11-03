from tkinter import*

noruega=Tk()
noruega.geometry("400x300")
noruega.resizable(0,0)
noruega.config(bg="red3")
#frame colummnablanca
columna_blanca=Frame(noruega)
columna_blanca.config(bg="ghost white",width=40,height=300)
columna_blanca.place(x=100,y=0)

fila_blanca=Frame(noruega)
fila_blanca.config(bg="ghost white",width=400,height=40)
fila_blanca.place(x=0,y=130)

columna_azul=Frame(noruega)
columna_azul.config(bg="midnight blue",width=20,height=300)
columna_azul.place(x=110,y=0)

fila_azul=Frame(noruega)
fila_azul.config(bg="midnight blue",width=400,height=20)
fila_azul.place(x=0,y=140)

noruega.mainloop()