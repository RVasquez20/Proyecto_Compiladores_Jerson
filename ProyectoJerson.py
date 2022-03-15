import tkinter as tk
import tkinter.filedialog as fd
from venv import main

main = tk.Tk()
main.title("Proyecto de Compiladores")
main.columnconfigure(0 ,weight=1)
main.rowconfigure(0 ,weight=2)
main.rowconfigure(1, minsize=2)
main.rowconfigure(2, weight=1)

#Funcion para colocar texto en cuadro
def llenar_Texto(lineas):
    Texto.delete(1.0,tk.END)
    Texto.insert(1.0,lineas)

#Funcion de Abrir Archivo

def abrir_Archivo():
    url = fd.askopenfilename(title = "Abrir Archivos",filetypes=(("Archivos de Texto","*.txt"),("Todos los Archivos","*.*")))
    file = open(url,'r')
    lines=''
    for line in file:
        lines+=line
    #llenar_Texto(file.read())
    llenar_Texto(lines)
    file.close()
    

#Menu
menu_Principal = tk.Menu(main)
menu_Archivo= tk.Menu(main,tearoff=False)
menu_Principal.add_cascade(label = "Archivo",menu=menu_Archivo)
menu_Archivo.add_command(label="Abrir",command = abrir_Archivo)



# Cuadro de texto

Texto = tk.Text(main)
Texto.grid(row = 0, column = 0, sticky = 'nswe',padx = 10, pady =5)

#Label 
Titulo=tk.Label(main, text='Manejador de Errores')
Titulo.grid(row = 1, column = 0, sticky = 'w', padx = 10)


# Manejador de Errores

Manejador_Errores = tk.Text(main,height =10)
Manejador_Errores.config(state=tk.DISABLED)
Manejador_Errores.grid(row = 2, column = 0, sticky = 'nswe',padx = 10, pady = 5)

#Scroll para el manejador de errores
scrollV = tk.Scrollbar(main, command=Manejador_Errores.yview)
scrollV.grid(row=2, column=1, sticky="nsew")

#Scroll para el cuadro de texto
scrollVCuadroTexto = tk.Scrollbar(main, command=Texto.yview)
scrollVCuadroTexto.grid(row=0, column=1, sticky="nsew")

Texto.config(yscrollcommand=scrollVCuadroTexto.set)
Manejador_Errores.config(yscrollcommand=scrollV.set)
main.config(menu=menu_Principal)
main.mainloop()