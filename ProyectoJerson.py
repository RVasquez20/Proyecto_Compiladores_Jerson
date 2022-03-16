from ctypes.wintypes import WORD
import tkinter as tk
import tkinter.font as tkf
import tkinter.filedialog as fd
from venv import main

main = tk.Tk()
main.title("Proyecto de Compiladores")
main.columnconfigure(0 ,weight=1)
main.columnconfigure(1, minsize=2)
main.columnconfigure(2 ,weight=1)
main.columnconfigure(3, minsize=2)
main.rowconfigure(0, minsize=2)
main.rowconfigure(1 ,weight=2)
main.rowconfigure(2, minsize=2)
main.rowconfigure(3, weight=1)
#Icono
main.iconbitmap("icono.ico")

#Fuentes
FuenteTitulos = tkf.Font(
            family="JetBrains Mono",
            size=18,
        )


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
menu_Principal.add_command(label="Abrir",command = abrir_Archivo)
menu_Principal.add_command(label="Compilar")



# Cuadro de texto

Texto = tk.Text(main, wrap=tk.WORD)
Texto.grid(row = 1, column = 0, sticky = 'nswe',padx = 10, pady =5)

# Cuadro de texto Resultados

Resultados = tk.Text(main, wrap=tk.WORD)
Resultados.grid(row = 1, column = 2, sticky = 'nswe',padx = 10, pady =5)

# Manejador de Errores

Manejador_Errores = tk.Text(main,height =10, wrap=tk.WORD)
Manejador_Errores.config(state=tk.DISABLED)
Manejador_Errores.grid(row = 3,columnspan=3, sticky = 'nswe',padx = 10, pady = 5)


#Label 
##Titulo Codigo
CuadroCodigo=tk.Label(main, text='Contenido del Archivo',font=FuenteTitulos)
CuadroCodigo.grid(row = 0, column = 0, sticky = 'w', padx = 10)
##Titulo Resultados
CuadroResultados=tk.Label(main, text='Resultados',font=FuenteTitulos)
CuadroResultados.grid(row = 0, column = 2, sticky = 'w', padx = 10)
##Titulo Errres
Errores=tk.Label(main, text='Manejador de Errores',font=FuenteTitulos)
Errores.grid(row = 2, column = 0, sticky = 'w', padx = 10)



#Scroll para el manejador de errores
scrollV = tk.Scrollbar(main, command=Manejador_Errores.yview)
scrollV.grid(row=3, column=3, sticky="nsew")

#Scroll para el cuadro de texto
scrollVCuadroTexto = tk.Scrollbar(main, command=Texto.yview)
scrollVCuadroTexto.grid(row=1, column=1, sticky="nsew")

#Scroll para el cuadro de texto de Resultados
scrollVCuadroTextoResultados = tk.Scrollbar(main, command=Resultados.yview)
scrollVCuadroTextoResultados.grid(row=1, column=3, sticky="nsew")

Texto.config(yscrollcommand=scrollVCuadroTexto.set)
Resultados.config(yscrollcommand=scrollVCuadroTextoResultados.set)
Manejador_Errores.config(yscrollcommand=scrollV.set)
main.config(menu=menu_Principal)
main.mainloop()