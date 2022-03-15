import tkinter as tk
import tkinter.filedialog as fd
from venv import main

main = tk.Tk()
main.title("Proyecto de Compiladores")





#Funcion para colocar texto en cuadro
def llenar_Texto(lineas):
    Texto.delete(1.0,tk.END)
    Texto.insert(1.0,lineas)

#Funcion de Abrir Archivo

def abrir_Archivo():
    url = fd.askopenfilename(title = "Abrir Archivos",filetypes=(("Archivos de Texto","*.txt"),("Todos los Archivos","*.*")))
    file = open(url,'r')
    llenar_Texto(file.read())
    file.close()
    

#Menu
menu_Principal = tk.Menu(main)
menu_Archivo= tk.Menu(main,tearoff=False)
menu_Principal.add_cascade(label = "Archivo",menu=menu_Archivo)
menu_Archivo.add_command(label="Abrir",command = abrir_Archivo)



# Cuadro de texto

Texto = tk.Text(main)
Texto.grid(row = 0, column = 0, sticky = 'nswe')


main.config(menu=menu_Principal)
main.mainloop()