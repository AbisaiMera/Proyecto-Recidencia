from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import customtkinter

# Propiedades de la ventana
ventana = customtkinter.CTk()
ventana.geometry("700x600")
ventana.title("Principal")
ventana.config(bg="lightgray")

# 🔹 Cargar imagen correctamente con PIL
imagen = Image.open("Logo_CFE.png") 
imagen = imagen.resize((300, 100))
imagen_tk = ImageTk.PhotoImage(imagen)
imagen = imagen.convert("RGBA")

imagen2 = Image.open("Logo_Medicion.jpg") 
imagen2 = imagen2.resize((150, 150))
imagen_tk2 = ImageTk.PhotoImage(imagen2)
imagen2 = imagen2.convert("RGBA")

# Función para abrir otro programa
def cargar():
    RPE = rpe.get().strip()
    RPU = rpu.get().strip()
    Metodo = seleccion.get()

    if not RPE or not RPU:  # 📌 Verifica si los campos están vacíos
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
    else:
        Metodo = seleccion.get()
        ventana.destroy()
        subprocess.run(["python", "Carga_Ins.py", RPE, RPU, Metodo])  # Llama al siguiente programa


# Opciones del menú desplegable
metodos = ["Carga Instantanea", "Factor Ajuste", "Historial"]
seleccion = StringVar()
seleccion.set("Carga Instantanea")

# 🔹 Encabezado
encabezado = customtkinter.CTkFrame(ventana, width=700, height=125, fg_color="White", bg_color="Black")
encabezado.place(relx=0, rely=0)

img = customtkinter.CTkLabel(encabezado, image=imagen_tk, text=" ")
img.place(relx=0.025, rely=0.16)
img.image = imagen_tk

titutlo = customtkinter.CTkLabel(encabezado, text="COMISION FEDERAL DE ELECTRICIDAD \n DIVISION CENTRO ORIENTE \n ZONA DE DISTRIBUCION TULA", bg_color="White", fg_color="White", text_color="Black", font=("Arial", 16, "bold"))
titutlo.place(relx=0.33, rely=0.2)

img2 = customtkinter.CTkLabel(encabezado, image=imagen_tk2, text=" ")
img2.place(relx=0.825, rely=0.1)
img2.image = imagen_tk2

# Etiquetas y cajas de texto
container = customtkinter.CTkFrame(ventana, width=450, height=400, fg_color="Green", bg_color="Lightgray")
container.place(relx=0.2, rely=0.27)

lbl1 = customtkinter.CTkLabel(container, text="R.P.E",  bg_color="Green", fg_color="Green", text_color="White", width=160, height=40, font=("Arial", 16, "bold"))
lbl1.place(relx=0.1, rely=0.15)

rpe = customtkinter.CTkEntry(container, width=160, height=40, fg_color="White", bg_color="Green", text_color="Black")
rpe.place(relx=0.5, rely=0.15)

lbl2 = customtkinter.CTkLabel(container, text="R.P.U",  bg_color="Green", fg_color="Green", text_color="White", width=160, height=40, font=("Arial", 16, "bold"))
lbl2.place(relx=0.1, rely=0.4)

rpu = customtkinter.CTkEntry(container, width=160, height=40, fg_color="White", bg_color="Green", text_color="Black")
rpu.place(relx=0.5, rely=0.4)

lbl3 = customtkinter.CTkLabel(container, text="Metodo",  bg_color="Green", fg_color="Green", text_color="White", width=160, height=40, font=("Arial", 16, "bold"))
lbl3.place(relx=0.1, rely=0.65)

metodo = customtkinter.CTkOptionMenu(container, variable=seleccion, values=metodos, bg_color="Green", fg_color="White", text_color="Black",width=160, height=40, button_color="Gray", button_hover_color="Darkgray")
metodo.place(relx=0.5, rely=0.65)

btn1 = customtkinter.CTkButton(container, text="Aceptar",fg_color="Gray", bg_color="Green", width=150, height=40, font=("Arial", 14, "bold"), command=cargar, hover_color="Darkgray")
btn1.place(relx=0.35, rely=0.85)

ventana.mainloop()
