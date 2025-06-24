from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import customtkinter
import sys
import os

# Detectar tamaño de pantalla
root = Tk()
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
root.destroy()

# Escalar ventana al 80% de la pantalla
ventana = customtkinter.CTk()
ventana.geometry(f"{int(ancho_pantalla * 0.7)}x{int(alto_pantalla * 0.9)}")
ventana.title("Principal")
ventana.config(bg="lightgray")

# Escalar fuente
fuente_base = int(ancho_pantalla * 0.015)

# Cargar imágenes
imagen = Image.open("Imagenes/Logo_CFE.png").resize((int(ancho_pantalla*0.3), int(alto_pantalla*0.12)))
imagen_tk = ImageTk.PhotoImage(imagen.convert("RGBA"))

imagen2 = Image.open("Imagenes/Logo_Medicion.jpg").resize((int(ancho_pantalla*0.15), int(alto_pantalla*0.2)))
imagen_tk2 = ImageTk.PhotoImage(imagen2.convert("RGBA"))


# Función para abrir otro programa
def cargar():
    RPE = rpe.get().strip()
    RPU = rpu.get().strip()
    Metodo = seleccion.get()

    if not RPE or not RPU:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
    else:
        ventana.destroy()  # Cierra la ventana actual

    ruta_base = os.path.dirname(sys.executable)  # Ruta donde está el ejecutable actual

    # Evalúa el método seleccionado para cargar la ventana apropiada:
    if Metodo == "Carga Instantanea":
        exe = os.path.join(ruta_base, "Carga_Ins.exe")
    elif Metodo == "Factor Ajuste":
        exe = os.path.join(ruta_base, "Factor_Ajs.exe")
    elif Metodo == "Historial":
        exe = os.path.join(ruta_base, "Historial.exe")
    else:
        messagebox.showerror("Error", "Opción no reconocida")
        return
    
    subprocess.run([exe, RPE, RPU, Metodo])

# Opciones del menú desplegable
metodos = ["Carga Instantanea", "Factor Ajuste", "Historial"]
seleccion = StringVar()
seleccion.set("Carga Instantanea")

# Encabezado
encabezado = customtkinter.CTkFrame(ventana, fg_color="White", bg_color="Black")
encabezado.place(relx=0, rely=0, relwidth=1, relheight=0.2)

img = customtkinter.CTkLabel(encabezado, image=imagen_tk, text=" ")
img.place(relx=0.02, rely=0.1)
img.image = imagen_tk

titulo = customtkinter.CTkLabel(
    encabezado,
    text="COMISION FEDERAL DE ELECTRICIDAD \n DIVISION CENTRO ORIENTE \n ZONA DE DISTRIBUCION TULA",
    bg_color="White", fg_color="White", text_color="Black",
    font=("Arial", int(fuente_base * 1.1), "bold")
)
titulo.place(relx=0.33, rely=0.2)

img2 = customtkinter.CTkLabel(encabezado, image=imagen_tk2, text=" ")
img2.place(relx=0.82, rely=0.05)
img2.image = imagen_tk2

# Contenedor principal
container = customtkinter.CTkFrame(ventana, fg_color="Green", bg_color="Lightgray")
container.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.6)

# Campos de entrada
lbl1 = customtkinter.CTkLabel(container, text="R.P.E", text_color="White", font=("Arial", fuente_base, "bold"))
lbl1.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.1)

rpe = customtkinter.CTkEntry(container, fg_color="White", bg_color="Green", text_color="Black", font=("Arial", fuente_base))
rpe.place(relx=0.5, rely=0.15, relwidth=0.4, relheight=0.1)

lbl2 = customtkinter.CTkLabel(container, text="R.P.U", text_color="White", font=("Arial", fuente_base, "bold"))
lbl2.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

rpu = customtkinter.CTkEntry(container, fg_color="White", bg_color="Green", text_color="Black", font=("Arial", fuente_base))
rpu.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1)

lbl3 = customtkinter.CTkLabel(container, text="Metodo", text_color="White", font=("Arial", fuente_base, "bold"))
lbl3.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.1)

metodo = customtkinter.CTkOptionMenu(container, variable=seleccion, values=metodos, bg_color="Green", fg_color="White", 
                                     text_color="Black", button_color="Gray", button_hover_color="Darkgray", font=("Arial", fuente_base))
metodo.place(relx=0.5, rely=0.65, relwidth=0.4, relheight=0.1)
btn1 = customtkinter.CTkButton(
    container,
    text="Aceptar",
    fg_color="Gray",
    font=("Arial", fuente_base, "bold"),
    command=cargar,
    hover_color="Darkgray"
)
btn1.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.1)

ventana.mainloop()
