from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter
import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime, timedelta
import locale
from Database.Conexion_SQL_Server import *
from Database.Datos import * 
import sys

ventana = customtkinter.CTk()
ventana.title("Factor Ajuste")
ventana.config(bg="Lightgray")

# Obtener el tamaño de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Configurar la ventana para que ocupe todo el tamaño de la pantalla
ventana.geometry(f"{screen_width}x{screen_height}")

# Poner los elementos del programa en Español
locale.setlocale(locale.LC_TIME, "es_MX")

# sys.argv contiene los argumentos pasados
RPE = sys.argv[1]  # Primer argumento
RPU = sys.argv[2]    # Segundo argumento
# RPU = 272680903204
# RPE = "JA117"
# 🔹 Cargar imagen correctamente con PIL
imagen = Image.open("Imagenes/Logo_CFE.png") 
imagen = imagen.resize((400, 125))
imagen_tk = ImageTk.PhotoImage(imagen)
imagen = imagen.convert("RGBA")

imagen2 = Image.open("Imagenes/Logo_Medicion.jpg") 
imagen2 = imagen2.resize((175, 175))
imagen_tk2 = ImageTk.PhotoImage(imagen2)
imagen2 = imagen2.convert("RGBA")

# 🔹 Encabezado
encabezado = customtkinter.CTkFrame(ventana, width=screen_width, height=125, fg_color="White", bg_color="Black")
encabezado.place(relx=0, rely=0)

img = customtkinter.CTkLabel(encabezado, image=imagen_tk, text=" ")
img.place(relx=0.025, rely=0.15)
img.image = imagen_tk

titutlo = customtkinter.CTkLabel(encabezado, text="COMISION FEDERAL DE ELECTRICIDAD \n DIVISION CENTRO ORIENTE \n ZONA DE DISTRIBUCION TULA", bg_color="White", fg_color="White", text_color="Black", font=("Arial", 20, "bold"))
titutlo.place(relx=0.39, rely=0.2)

img2 = customtkinter.CTkLabel(encabezado, image=imagen_tk2, text=" ")
img2.place(relx=0.825, rely=0.02)
img2.image = imagen_tk2
# Fin de Encabezado

# Datos Generales
# Datos RPE
ListaRPE = {
"9L99B": "Francisco Javier Velazquez Cervantes",
"JA117": "Jerzael Abisai Mera Zapatero"
}

datos = customtkinter.CTkFrame(ventana, width=screen_width, height=110, fg_color="green", bg_color="Black")
datos.place(relx=0, y=125)

estiloDatos = { 
        "fg_color": ("Green"), 
        "bg_color": ("Green"), 
        "text_color": ("White"), 
        "width": 50, 
        "height": 20, 
        "font": ("Arial", 16,"bold")
}

def ExtraccionCuenta():
    texto = cuenta.cget("text")  # Obtener el texto del Label

    Cclo = texto[:2]        # Primeras 2 letras
    pblacion = texto[7:9]   # Caracteres 6 y 7
    rta = texto[9:12]       # 3 caracteres después
    flio = texto[12:16]       # Últimos 4 caracteres

    ciclo.configure(text=Cclo)
    poblacion.configure(text=pblacion)
    ruta.configure(text=rta)
    folio.configure(text=flio)

ahora = datetime.now()
fecha_hora = ahora.strftime("%A, %d %B, %Y")

lbl1 = customtkinter.CTkLabel(datos, text="R.P.E :", **estiloDatos)
lbl1.place(relx=0.05, rely=0.2)

rpe = customtkinter.CTkLabel(datos, text=RPE, **estiloDatos)
rpe.place(relx=0.1, rely=0.2)

lbl2 = customtkinter.CTkLabel(datos, text="Nombre :", **estiloDatos)
lbl2.place(relx=0.25, rely=0.2)

Nomrpe = customtkinter.CTkLabel(datos, text="Nombre del RPE", **estiloDatos)
Nomrpe.place(relx=0.3, rely=0.2)

FechaAct = customtkinter.CTkLabel(datos, text=fecha_hora, **estiloDatos)
FechaAct.place(relx=0.84, rely=0.2)

# Buscar el RPE dentro del diccionario de trabajadores
nombre_rpe = ListaRPE.get(RPE, "Trabajador no encontrado")  # Si no está en el diccionario, muestra "Trabajador no encontrado"
    
Nomrpe.configure(text=nombre_rpe)

# Datos RPU - Fila 1
DatosRPU = BD.datosRPU(RPU)
MedidoresRPU = BD.medidores(RPU)

lbl3 = customtkinter.CTkLabel(datos, text="R.P.U :", **estiloDatos)
lbl3.place(relx=0.05, rely=0.4)

rpu = customtkinter.CTkLabel(datos, text=RPU, **estiloDatos)
rpu.place(relx=0.1, rely=0.4)

lbl4 = customtkinter.CTkLabel(datos, text="Cuenta :", **estiloDatos)
lbl4.place(relx=0.25, rely=0.4)

cuenta = customtkinter.CTkLabel(datos, text="23DV13B162333130", **estiloDatos)
cuenta.place(relx=0.3, rely=0.4)

lbl5 = customtkinter.CTkLabel(datos, text="Nombre :", **estiloDatos)
lbl5.place(relx=0.45, rely=0.4)

Nomrpu = customtkinter.CTkLabel(datos, text="Nombre del RPU", **estiloDatos)
Nomrpu.place(relx=0.5, rely=0.4)

lbl6 = customtkinter.CTkLabel(datos, text="Medidor :", **estiloDatos)
lbl6.place(relx=0.65, rely=0.4)

medidores = [registro[1] for registro in MedidoresRPU]
selected_medidor = ctk.StringVar()
selected_medidor.set(medidores[0] if medidores else "")

medidor = customtkinter.CTkOptionMenu(datos, variable=selected_medidor ,values=medidores, **estiloDatos)
medidor.place(relx=0.7, rely=0.4)

# Datos RPU - Fila 2
lbl7 = customtkinter.CTkLabel(datos, text="Ciclo :",  **estiloDatos)
lbl7.place(relx=0.05, rely=0.6)

ciclo = customtkinter.CTkLabel(datos, text=" ", **estiloDatos)
ciclo.place(relx=0.1, rely=0.6)

lbl8 = customtkinter.CTkLabel(datos, text="Poblacion :", **estiloDatos)
lbl8.place(relx=0.25, rely=0.6)

poblacion = customtkinter.CTkLabel(datos, text=" ", **estiloDatos)
poblacion.place(relx=0.3, rely=0.6)

lbl9 = customtkinter.CTkLabel(datos, text="Ruta :", **estiloDatos)
lbl9.place(relx=0.45, rely=0.6)

ruta = customtkinter.CTkLabel(datos, text=" ", **estiloDatos)
ruta.place(relx=0.5, rely=0.6)

lbl10 = customtkinter.CTkLabel(datos, text="Folio :", **estiloDatos)
lbl10.place(relx=0.65, rely=0.6)

folio = customtkinter.CTkLabel(datos, text=" ", **estiloDatos)
folio.place(relx=0.7, rely=0.6)

lbl11 = customtkinter.CTkLabel(datos, text="Agencia :", **estiloDatos)
lbl11.place(relx=0.85, rely=0.6)

agencia = customtkinter.CTkLabel(datos, text="Nombre de la Agencia", **estiloDatos)
agencia.place(relx=0.9, rely=0.6)

# Diccionario de las agencias
AGENCIAS = {
    "A": "Progreso",
    "B": "Tula",
    "C": "Tlaxcoapan",
    "D": "Tepeji"
}

# Cargar Datos de RPU de la BD en las etiquetas

if DatosRPU and len(DatosRPU) >= 4:
    Nomrpu.configure(text=DatosRPU[1])  # Nombre RPU
    cuenta.configure(text=DatosRPU[2])  # Cuenta

     # Obtener la agencia del resultado
    codigo_agencia = DatosRPU[3]
    
    # Convertir el código a su nombre correspondiente
    nombre_agencia = AGENCIAS.get(codigo_agencia, "Desconocida")  # Si no está en el diccionario, muestra "Desconocida"
    
    agencia.configure(text=nombre_agencia)
else:
    # Si no hay datos, mostrar un mensaje de "No encontrado"
    Nomrpu.configure(text="No encontrado")
    cuenta.configure(text="No encontrado")
    agencia.configure(text="No encontrado")

# Fin de Datos Generales

# Llamar a la función inmediatamente al inicio
ExtraccionCuenta()

# Seccion de Calculos
calculos = customtkinter.CTkFrame(ventana, width=600, height=655, fg_color="gray", bg_color="Black")
calculos.place(relx=0, y=235)

lbl12 = customtkinter.CTkLabel(calculos, text="BASE DE CALCULO PARA REALIZAR AJUSTE", fg_color="Gray", bg_color="Gray", text_color="White", width=75, height=20, font=("Arial", 16,"bold"))
lbl12.place(relx=0.22, rely=0.02)

# Tabla
class TablaApp(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=600, height=500, fg_color="#2b2b2b", bg_color="#2b2b2b")
        self.place(relx=0.02, y=42)

        self.canvas = ctk.CTkCanvas(self, width=860, height=90, bg="#2b2b2b")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.table_frame = ctk.CTkFrame(self.canvas, fg_color="#2b2b2b", bg_color="#2b2b2b")
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        self.table = []
        self.create_table()

        self.table_frame.bind("<Configure>", self.on_frame_configure)

    def create_table(self):
        headers = ["Corriente", "Voltaje", "kVA real", "kVA cronometro", "% Registración"]
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(self.table_frame, text=header, fg_color="Green", bg_color="Green", text_color="White", width=112, height=25, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col, padx=1, pady=1)

        for _ in range(1):  # Agrega 1 fila inicial
            self.add_row()

    def add_row(self):
        row = []
        for j in range(5):  
            entry = ctk.CTkEntry(self.table_frame, width=112, height=30, fg_color="White", bg_color="White", border_color="White", text_color="Black")
            entry.grid(row=len(self.table) + 1, column=j, padx=1, pady=1)
            row.append(entry)
        self.table.append(row)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

tabla = TablaApp(calculos)
# Fin de la tabla

# Apartado del Periodo
lbl13 = customtkinter.CTkLabel(calculos, text="Periodo", fg_color="Gray", bg_color="Gray", text_color="White", width=75, height=20, font=("Arial", 16,"bold"))
lbl13.place(relx=0.05, rely=0.18)

class PeriodoSelector(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, width=540, height=100)
        self.pack_propagate(False)

        # Label Desde
        self.label_desde = ctk.CTkLabel(self, text="Desde (Año-Mes-Día):")
        self.label_desde.place(relx=0.2, rely=0.1)

        # Selector de fecha "Desde" (Formato completo)
        self.date_desde = DateEntry(self, width=10, background='darkgreen', 
                                    foreground='white', borderwidth=2, year=2025, 
                                    date_pattern="yyyy-mm-dd", font=(14))  
        self.date_desde.place(relx=0.23, rely=0.5)

        # Label Hasta
        self.label_hasta = ctk.CTkLabel(self, text="Hasta (Año-Mes-Día):")
        self.label_hasta.place(relx=0.55, rely=0.1)

        # Selector de fecha "Hasta" (Formato completo)
        self.date_hasta = DateEntry(self, width=10, background='darkgreen', 
                                    foreground='white', borderwidth=2, year=2025, 
                                    date_pattern="yyyy-mm-dd", font=(14))  
        self.date_hasta.place(relx=0.57, rely=0.5)

    def get_range(self):
        # Obtener la fecha seleccionada y mostrarla con Año-Mes-Día
        desde_año = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%Y")
        desde_mes = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%m")
        desde_mes_palabra = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%B")
        desde_dia = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%d")

        hasta_año = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%Y")
        hasta_mes = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%m")
        hasta_mes_palabra = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%B")
        hasta_dia = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%d")
        
        return desde_año, desde_mes, desde_mes_palabra, desde_dia, hasta_año, hasta_mes, hasta_mes_palabra, hasta_dia


periodo_selector = PeriodoSelector(calculos)
periodo_selector.place(relx=0.05, rely=0.22)  # Ajusta la posición
# Fin del Apartado Periodo

lbl14 = customtkinter.CTkLabel(calculos, text="Anomalia :", fg_color="Gray", bg_color="Gray", text_color="White", width=75, height=20, font=("Arial", 16,"bold"))
lbl14.place(relx=0.05, rely=0.40)

anomalia = customtkinter.CTkEntry(calculos, width=100, height=20, fg_color="White", bg_color="Gray", text_color="Black")
anomalia.place(relx=0.2, rely=0.40)

class PeriodoIncompleto(ctk.CTkFrame):
    def __init__(self, master=None, periodo_selector=None):
        super().__init__(master, width=540, height=100)
        self.pack_propagate(False)

        self.periodo_selector = periodo_selector  # Guardamos la referencia del PeriodoSelector

        # Label Desde
        self.label_desde = ctk.CTkLabel(self, text="Desde (Año-Mes-Día):")
        self.label_desde.place(relx=0.2, rely=0.1)

        # Selector de fecha "Desde" (Formato completo)
        self.date_desde = DateEntry(self, width=10, background='darkred', 
                                    foreground='white', borderwidth=2, year=2025, 
                                    date_pattern="yyyy-mm-dd", font=(14))  
        self.date_desde.place(relx=0.23, rely=0.5)

        # Label Hasta
        self.label_hasta = ctk.CTkLabel(self, text="Hasta (Año-Mes-Día):")
        self.label_hasta.place(relx=0.55, rely=0.1)

        # Selector de fecha "Hasta" (Formato completo)
        self.date_hasta = DateEntry(self, width=10, background='darkred', 
                                    foreground='white', borderwidth=2, year=2025, 
                                    date_pattern="yyyy-mm-dd", font=(14))  
        self.date_hasta.place(relx=0.57, rely=0.5)

    def get_range(self):
       
        # Obtener la fecha seleccionada y mostrarla con Año-Mes-Día
        incompleto_desde_año = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%Y")
        incompleto_desde_mes = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%m")
        incompleto_desde_mes_palabra = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%B")
        incompleto_desde_dia = datetime.strptime(self.date_desde.get(), "%Y-%m-%d").strftime("%d")

        incompleto_hasta_año = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%Y")
        incompleto_hasta_año_formato = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%Y")[-2:]
        incompleto_hasta_mes = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%m")
        incompleto_hasta_mes_palabra = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%B")
        incompleto_hasta_dia = datetime.strptime(self.date_hasta.get(), "%Y-%m-%d").strftime("%d")
        
        return incompleto_desde_año, incompleto_desde_mes, incompleto_desde_mes_palabra, incompleto_desde_dia, incompleto_hasta_año, incompleto_hasta_año_formato, incompleto_hasta_mes, incompleto_hasta_mes_palabra, incompleto_hasta_dia


lbl34 = customtkinter.CTkLabel(calculos, text="Periodo Incompleto", fg_color="Gray", bg_color="Gray", text_color="White", width=75, height=20, font=("Arial", 16,"bold"))
lbl34.place(relx=0.05, rely=0.48)

periodo_selector_incompleto = PeriodoIncompleto(calculos, periodo_selector)
periodo_selector_incompleto.place(relx=0.05, rely=0.53)  # Ajusta la posición
# Fin del apartado de Periodo Incompleto

# Apartado para Lectura Inicial y Lectura Final
lbl35 = customtkinter.CTkLabel(calculos, text="Lectura Inicial", fg_color="Gray", bg_color="Gray", text_color="White", width=75, height=20, font=("Arial", 16,"bold"))
lbl35.place(relx=0.2, rely=0.73)

LectInic = customtkinter.CTkEntry(calculos, width=100, height=20, fg_color="White", bg_color="Gray", text_color="Black")
LectInic.place(relx=0.2, rely=0.78)

lbl36 = customtkinter.CTkLabel(calculos, text="Lectura Final", fg_color="Gray", bg_color="Gray", text_color="White", width=75, height=20, font=("Arial", 16,"bold"))
lbl36.place(relx=0.6, rely=0.73)

LectFin = customtkinter.CTkEntry(calculos, width=100, height=20, fg_color="White", bg_color="Gray", text_color="Black")
LectFin.place(relx=0.6, rely=0.78)
# Fin del apartado para Lectura Inicial y Lectura Final

def Calculos():
    columnas = [0] * 5
    conteo = [0] * 5  # Para contar cuántos valores válidos hay en cada columna

    for row in tabla.table:
        for col, entry in enumerate(row):
            try:
                value = entry.get().strip()
                if value:
                    columnas[col] += float(value)
                    conteo[col] += 1
            except ValueError:
                pass # Ignorar valores no numéricos

    # Calcular promedios con manejo de división por cero
    factordeajuste = (1 / columnas[4]) * 100 if columnas[4] > 0 else 0

    # Asignar valores a las etiquetas correspondientes
    corriente.configure(text=f"{columnas[0]:.1f}")
    voltaje.configure(text=f"{columnas[1]:.1f}")
    kvareal.configure(text=f"{columnas[2]:.4f}")
    kvacronometro.configure(text=f"{columnas[3]:.4f}")
    registracion.configure(text=f"{columnas[4]:.3f}")
    FactAjus.configure(text=f"{factordeajuste:.4f}")

    # Limpiar la tabla antes de insertar nuevos datos
    Tabla.delete(*Tabla.get_children())

    try:
        FA = float(FactAjus.cget("text"))
    except ValueError:
        FA = 0  

    # Variables para obtener los cálculos
    suma_dias = 0
    suma_kWh_total = 0
    suma_kWh_total_DF = 0
    suma_kWh_total_D = 0

    MedSelect = selected_medidor.get()

    tarifa = BD.tarifa(RPU, MedSelect)
    lbl25.configure(text=tarifa[0])

    # Mostrar los datos en la tabla
    rpu = RPU

    desde_año, desde_mes, desde_mes_palabra, desde_dia, hasta_año, hasta_mes, hasta_mes_palabra, hasta_dia = periodo_selector.get_range()
    desde = f"{desde_año}-{desde_mes}-{desde_dia}"
    hasta = f"{hasta_año}-{hasta_mes}-{hasta_dia}"
    
    for row in BD.mostrardatos(rpu, desde, hasta):
        FECHA, DESDE, HASTA, CONSUMO = row

        # Convertir CONSUMO a entero si es necesario
        if isinstance(CONSUMO, str):
            CONSUMO = int(CONSUMO)

        # Formatear la fecha para mostrar los últimos 2 dígitos del año y los 2 dígitos del mes
        FECHA_FORMATO = FECHA.strftime('%y%m')

        # Formatear las fechas desde y hasta para mostrar solo la fecha y no la hora
        DESDE_FORMATO = DESDE.strftime('%Y-%m-%d')
        HASTA_FORMATO = HASTA.strftime('%Y-%m-%d')

        # Calcular nuevas columnas
        DIAS = (HASTA - DESDE).days
        CONSUMO_DF = round(FA * CONSUMO)  # Redondear hacia arriba o abajo
        CONSUMO_D = round(CONSUMO_DF - CONSUMO)  # Redondear hacia arriba o abajo

        if 58 <= DIAS <= 63:
            # Insertar en la tabla en orden cronológico
            Tabla.insert("", "end", values=(FECHA_FORMATO, DESDE_FORMATO, HASTA_FORMATO, DIAS, CONSUMO, CONSUMO_DF, CONSUMO_D))

            # Acumular sumas
            suma_dias += DIAS
            suma_kWh_total += CONSUMO
            suma_kWh_total_DF += CONSUMO_DF
            suma_kWh_total_D += CONSUMO_D
    
    totalDias.configure(text=suma_dias)
    totalCFRkwh.configure(text=suma_kWh_total)
    totalDFkwh.configure(text=suma_kWh_total_DF)
    totalDkwh.configure(text=suma_kWh_total_D)
    lbl28.configure(text=suma_kWh_total_D)

    # Diccionario de anomalias
    Anomalias = {
        "EF01": "DIRECTO CON ESTIMACION ERRÓNEA",
        "EF02": "TARIFA INCORRECTA",
        "EF03": "SERVICIO CON LECTURAS ESTIMADAS",
        "EF04": "SERVICIO CON MEDICIÓN Y NO SE FACTURA",
        "EF05": "SERVICIO DE CONCURRENCIA DE TARIFAS",
        "EF06": "LECTURA MAL TOMADA",
        "EF07": "CARGA MAYOR A LA CONTRATADA",
        "EF08": "MULTIPLICADOR DE LECTURAS ERRÓNEO",
        "EF09": "CLAVE DE TIPO DE SUMINISTRO ERRÓNEA",

        "FM01": "SERVICIO DIRECTO",
        "FM02": "MULTIPLICADOR DE LECTURAS ERRÓNEO",
        "FM03": "MEDIDOR MAL CONECTADO",
        "FM04": "BOBINA DE POTENCIAL ABIERTA",
        "FM05": "MEDIDOR QUEMADO",
        "FM06": "TRANSFORMADOR DE INSTRUMENTO DAÑADO",
        "FM07": "TRANSFORMADOR DE INSTRUMENTO MAL CONTECTADO",
        "FM08": "CIRCUTIO DE CORRIENTE DE T.C A TIERRA",
        "FM09": "REGISTRO SIN ENGRANAR",
        "FM10": "NÚMERO DE MEDIDOR DIFERENTE AL DE FACTURACION",
        "FM11": "CLAVE DE TIPO DE SUMINISTRO MAL ERRÓNEA",
        "FM12": "MEDICION INADECUADA AL CIRCUITO",
        "FM13": "MEDIDOR DESTRUIDO",
        "FM14": "ALAMBRADO SECUNDARIO DAÑADO",
        "FM15": "SECUDNARIO DE T.C. EN CORTO CIRCUITO",
        "FM16": "MEDIDOR MAL PROGRAMADO",
        "FM17": "REGISTRO ATORADO",
        "FM18": "DISCO ATORADO",

        "UI01": "SELLOS VIOLADOS",
        "UI02": "SELLO FALSIFICADO",
        "UI03": "SERVICIO DIRECTO SIN CONTRATO",
        "UI04": "CARGA CONECTADA ANTES DE LA MEDICIÓN",
        "UI05": "MANECILLAS INVERTIDAS",
        "UI06": "DISCO ATORADO",
        "UI07": "AJUSTE DE MEDIDORES MOVIDOS",
        "UI08": "RETORNO DE CORRIENTE ABIERTO",
        "UI09": "INTERVENCIÓN DE LAS CONEXIONES DEL EQUIPO",
        "UI10": "ALDABAS DE POTENCILA ABIERTAS",
        "UI11": "MEDIDOR INVERTIDO",
        "UI12": "TERMINALES DE BASE ENCHUFES PUENTEADAS",
        "UI13": "SIN CONTRATO CON MEDICIÓN INSTALADA",
        "UI14": "PASA ENERGÍA A OTRO DOMICILIO",
        "UI15": "ALTERACIÓN A LA PROGRAMACIÓN DEL MEDIDOR",
        "UI16": "RETIRA SU MEDIDOR Y COLOCA OTRO QUE NO FACTURA",
        "UI17": "REGISTRO DEL MEDIDOR ALTERADO O CAMBIADO",
        "UI18": "OTROS USOS INDEBIDOS"
    }

    # Obtener fechas del periodo_selector
    items = Tabla.get_children()
    if not items:
        messagebox.showerror("Error", "⚠ No hay datos en la tabla para validar.")
        return False

    # Tomar el primer y último registro de la tabla
    primer_registro = Tabla.item(items[0], "values")  # Primer registro
    ultimo_registro = Tabla.item(items[-1], "values")  # Último registro

    desde_año_txt = datetime.strptime(primer_registro[1], "%Y-%m-%d").strftime("%Y")
    desde_mes_palabra_txt = datetime.strptime(primer_registro[1], "%Y-%m-%d").strftime("%B")
    desde_dia_txt = datetime.strptime(primer_registro[1], "%Y-%m-%d").strftime("%d")

    hasta_año_txt = datetime.strptime(ultimo_registro[2], "%Y-%m-%d").strftime("%Y")
    hasta_mes_palabra_txt = datetime.strptime(ultimo_registro[2], "%Y-%m-%d").strftime("%B")
    hasta_dia_txt = datetime.strptime(ultimo_registro[2], "%Y-%m-%d").strftime("%d")

    lbl31.configure(text=f"Del {desde_dia_txt} de {desde_mes_palabra_txt} de {desde_año_txt} al {hasta_dia_txt} de {hasta_mes_palabra_txt} de {hasta_año_txt}")

    codigo_anomalia = anomalia.get()
    nombre_anomalia = Anomalias.get(codigo_anomalia, "Desconocida")  # Si no está en el diccionario, muestra "Desconocida"
    lbl33.configure(text=nombre_anomalia)

    return suma_dias, suma_kWh_total, suma_kWh_total_DF, suma_kWh_total_D, rpu, desde, hasta

cargar = ctk.CTkButton(calculos, text="Calcular",fg_color="#2b2b2b", bg_color="Gray", width=100, height=40, font=("Arial", 14, "bold"), hover_color="Green", command=Calculos)
cargar.place(relx=0.6, rely=0.40)

def Agregar():

    suma_dias, suma_kWh_total, suma_kWh_total_DF, suma_kWh_total_D, rpu, desde, hasta = Calculos()
    incompleto_desde_año, incompleto_desde_mes, incompleto_desde_mes_palabra, incompleto_desde_dia, incompleto_hasta_año, incompleto_hasta_año_formato, incompleto_hasta_mes, incompleto_hasta_mes_palabra, incompleto_hasta_dia = periodo_selector_incompleto.get_range()
    
    # Primero, validar que las fechas del periodo incompleto sean correctas
    if not validar_fecha(rpu, desde, hasta):
        return  # Si la validación falla, no continuar con la inserción

    # Colocar fechas de periodo incompleto en la tabla
    desde_incompleto = f"{incompleto_desde_año}-{incompleto_desde_mes}-{incompleto_desde_dia}"
    hasta_incompleto = f"{incompleto_hasta_año}-{incompleto_hasta_mes}-{incompleto_hasta_dia}"
    fecha_incompleto = f"{incompleto_hasta_año_formato}{incompleto_hasta_mes}"

    # Convertir strings a objetos datetime
    desde_incompleto_formato = datetime.strptime(desde_incompleto, "%Y-%m-%d").date()
    hasta_incompleto_formato = datetime.strptime(hasta_incompleto, "%Y-%m-%d").date()

    # Calcular la diferencia en días
    dias_incompletos = (hasta_incompleto_formato - desde_incompleto_formato).days

    try:
        FA = float(FactAjus.cget("text"))
        LI = int(LectInic.get())
        LF = int(LectFin.get())
    except ValueError:
        FA = 0
        LI = 0
        LF = 0 

    if LI > LF:
        diferencia = LI - LF
    else:
        diferencia = LF - LI
    
    consumo_incompleto_DF  = round(diferencia * FA)  # Redondear hacia arriba o abajo
    consumo_incompleto = 0
    consumoDF_incompleto = round(consumo_incompleto_DF  - 0)  # Redondear hacia arriba o abajo

    # Convertir las fechas de cadena a objetos datetime.date
    fecha_incompleto_dt = datetime.strptime(fecha_incompleto, "%y%m").date()

    # Obtener todas las filas actuales en la tabla
    filas = Tabla.get_children()
    valores = None  # Inicializar valores como None

   # Verificar si la tabla tiene datos
    if filas:
        # Obtener la primera fila para comparar la fecha más antigua
        primera_fila = filas[0]
        valores = Tabla.item(primera_fila, "values")

        # Verificar si hay datos válidos antes de acceder a valores[0]
        if valores and len(valores) > 0:
            try:
                fecha_bd_dt = datetime.strptime(valores[0], "%y%m").date()
            except ValueError:
                print(f"⚠ Error: No se pudo convertir la fecha '{valores[0]}' a datetime.")
                return  # Salimos de la función en caso de error

            # Comparar fechas para insertar correctamente
            if fecha_incompleto_dt < fecha_bd_dt:
                # Insertar al principio
                Tabla.insert("", "0", values=(fecha_incompleto, desde_incompleto, hasta_incompleto, dias_incompletos, consumo_incompleto, consumo_incompleto_DF, consumoDF_incompleto))
            else:
                # Insertar al final
                Tabla.insert("", "end", values=(fecha_incompleto, desde_incompleto, hasta_incompleto, dias_incompletos, consumo_incompleto, consumo_incompleto_DF, consumoDF_incompleto))
        else:
            print("⚠ Error: No se encontraron valores válidos en la tabla.")
    else:
        # Si la tabla está vacía, insertar directamente
        Tabla.insert("", "end", values=(fecha_incompleto, desde_incompleto, hasta_incompleto, dias_incompletos, consumo_incompleto, consumo_incompleto_DF, consumoDF_incompleto))
    
    # 3️⃣ Sumamos los valores del periodo incompleto
    suma_dias += dias_incompletos
    suma_kWh_total_DF += consumo_incompleto_DF
    suma_kWh_total_D += consumoDF_incompleto

    # 4️⃣ Actualizamos las etiquetas
    totalDias.configure(text=suma_dias)
    totalDFkwh.configure(text=suma_kWh_total_DF)
    totalDkwh.configure(text=suma_kWh_total_D)
    lbl28.configure(text=suma_kWh_total_D)

def insertar_en_orden(tabla, nueva_fecha, valores):
    """Inserta una fila en orden cronológico dentro de la tabla"""
    filas = tabla.get_children()
    posicion = None

    # Convertir nueva fecha a número para comparación
    nueva_fecha = int(nueva_fecha)

    for fila in filas:
        fila_valores = tabla.item(fila, "values")
        fecha_existente = int(fila_valores[0])  # Primera columna es la fecha

        if nueva_fecha < fecha_existente:
            posicion = fila  # Insertar antes de esta fila
            break

    if posicion:
        tabla.insert("", "before", posicion, values=valores)  # 🔹 Insertar en orden
    else:
        tabla.insert("", "end", values=valores)  # Si no encontró, insertar al final

def validar_fecha(rpu, desde, hasta):
    # Consultar la base de datos para obtener los registros
    datos_bd = BD.mostrardatos(rpu, desde, hasta)
    
    # Verificar si hay datos en la BD
    if not datos_bd:
        messagebox.showerror("Error", "⚠ No hay datos en la base de datos para validar.")
        return False

    # Obtener la fecha más antigua y la más reciente en la BD
    fechas_desde = [registro[1].date() for registro in datos_bd]  # "DESDE"
    fechas_hasta = [registro[2].date() for registro in datos_bd]  # "HASTA"
    
    fecha_desde_bd = min(fechas_desde)  # Primer registro en la BD
    fecha_hasta_bd = max(fechas_hasta)  # Último registro en la BD

    # Obtener fechas del periodo incompleto
    periodo_desde = datetime.strptime(periodo_selector_incompleto.date_desde.get(), "%Y-%m-%d").date()
    periodo_hasta = datetime.strptime(periodo_selector_incompleto.date_hasta.get(), "%Y-%m-%d").date()

    # Validar si el periodo incompleto se solapa con el periodo principal de la BD
    if (fecha_desde_bd < periodo_desde < fecha_hasta_bd) or (fecha_desde_bd < periodo_hasta < fecha_hasta_bd):
        messagebox.showerror("Error", "⚠ Las fechas seleccionadas están dentro del período principal.")
        return False  # Validación fallida

    incompleto_desde_año, incompleto_desde_mes, incompleto_desde_mes_palabra, incompleto_desde_dia, incompleto_hasta_año, incompleto_hasta_año_formato, incompleto_hasta_mes, incompleto_hasta_mes_palabra, incompleto_hasta_dia = periodo_selector_incompleto.get_range()
    # Obtener la fecha seleccionada y mostrarla con Año-Mes-Día
    desde_año = fecha_desde_bd.strftime("%Y")
    desde_mes_palabra = fecha_desde_bd.strftime("%B")
    desde_dia = fecha_desde_bd.strftime("%d")

    hasta_año = fecha_hasta_bd.strftime("%Y")
    hasta_mes_palabra = fecha_hasta_bd.strftime("%B")
    hasta_dia = fecha_hasta_bd.strftime("%d")

    if periodo_desde >= fecha_hasta_bd: 
        lbl31.configure(text=f"Del {desde_dia} de {desde_mes_palabra} de {desde_año} al {incompleto_hasta_dia} de {incompleto_hasta_mes_palabra} de {incompleto_hasta_año}")
    elif periodo_hasta <= fecha_desde_bd: 
        lbl31.configure(text=f"Del {incompleto_desde_dia} de {incompleto_desde_mes_palabra} de {incompleto_desde_año} al {hasta_dia} de {hasta_mes_palabra} de {hasta_año}")

    return True  # Validación exitosa

agregar = ctk.CTkButton(calculos, text="Agregar",fg_color="#2b2b2b", bg_color="Gray", width=100, height=40, font=("Arial", 14, "bold"), hover_color="#FFC300", command=Agregar)
agregar.place(relx=0.4, rely=0.88)
# Fin de Seccion de Calculos

# Seccion de Tabla de resultados
ResultadosTabla = customtkinter.CTkFrame(ventana, width=850, height=100, fg_color="Black", bg_color="Black")
ResultadosTabla.place(relx=0.43, rely=0.3)

estiloTablaTitulo = { 
        "fg_color": ("#2fd134"), 
        "bg_color": ("#2fd134"), 
        "text_color": ("White"), 
        "width": 137, 
        "height": 38, 
        "font": ("Arial", 16,"bold")
}

estiloTablaDatos = { 
        "fg_color": ("White"), 
        "bg_color": ("White"), 
        "text_color": ("Black"), 
        "width": 137, 
        "height": 30, 
        "font": ("Arial", 16)
}

estiloTablaFinal = { 
        "fg_color": ("White"), 
        "bg_color": ("White"), 
        "text_color": ("Black"), 
        "width": 120, 
        "height": 40, 
        "font": ("Arial", 16, "bold")
}

col1 = customtkinter.CTkLabel(ResultadosTabla, text="Corriente", **estiloTablaTitulo)
col1.grid(row=1, column=1, padx=1, pady=1)

corriente = customtkinter.CTkLabel(ResultadosTabla, text="0.00", **estiloTablaDatos)
corriente.grid(row=2, column=1, padx=1, pady=1)

col2 = customtkinter.CTkLabel(ResultadosTabla, text="Voltaje", **estiloTablaTitulo)
col2.grid(row=1, column=2, padx=1, pady=1)

voltaje = customtkinter.CTkLabel(ResultadosTabla, text="0.00", **estiloTablaDatos)
voltaje.grid(row=2, column=2, padx=1, pady=1)

col3 = customtkinter.CTkLabel(ResultadosTabla, text="kVA real", **estiloTablaTitulo)
col3.grid(row=1, column=3, padx=1, pady=1)

kvareal = customtkinter.CTkLabel(ResultadosTabla, text="0.00", **estiloTablaDatos)
kvareal.grid(row=2, column=3, padx=1, pady=1)

col4 = customtkinter.CTkLabel(ResultadosTabla, text="kVA Cronometro", **estiloTablaTitulo)
col4.grid(row=1, column=4, padx=1, pady=1)

kvacronometro = customtkinter.CTkLabel(ResultadosTabla, text="0.00", **estiloTablaDatos)
kvacronometro.grid(row=2, column=4, padx=1, pady=1)

col5 = customtkinter.CTkLabel(ResultadosTabla, text="% Registración", **estiloTablaTitulo)
col5.grid(row=1, column=5, padx=1, pady=1)

registracion = customtkinter.CTkLabel(ResultadosTabla, text="0.00", **estiloTablaDatos)
registracion.grid(row=2, column=5, padx=1, pady=1)

col6 = customtkinter.CTkLabel(ResultadosTabla, text="FACTOR DE\n AJUSTE", **estiloTablaTitulo)
col6.grid(row=1, column=6, padx=1, pady=1)

FactAjus = customtkinter.CTkLabel(ResultadosTabla, text="0.00", **estiloTablaDatos)
FactAjus.grid(row=2, column=6, padx=1, pady=1)

TablaFinal = customtkinter.CTkFrame(ventana, width=850, height=450, fg_color="Black", bg_color="Black")
TablaFinal.place(relx=0.43, rely=0.4)

lbl15 = customtkinter.CTkLabel(TablaFinal, text="Consumos facturados\n reflejados en SICOM", width=591, height=40, fg_color="#fff301", bg_color="#fff301", text_color="Black", font=("Arial", 16,"bold"))
lbl15.grid(row=1, column=1, columnspan=4, padx=1, pady=1)

lbl16 = customtkinter.CTkLabel(TablaFinal, text="Debio\n facturar", width=120, height=40, fg_color="Orange", bg_color="Orange", text_color="Black", font= ("Arial", 16,"bold"))
lbl16.grid(row=1, column=5, padx=1, pady=1)

lbl17 = customtkinter.CTkLabel(TablaFinal, text="Diferencia", width=120, height=40, fg_color="#ff0000", bg_color="#ff0000", text_color="Black", font=("Arial", 16,"bold"))
lbl17.grid(row=1, column=6, padx=1, pady=1)

lbl18 = customtkinter.CTkLabel(TablaFinal, text="Fecha", **estiloTablaFinal)
lbl18.grid(row=2, column=1, padx=1, pady=1)

lbl19 = customtkinter.CTkLabel(TablaFinal, text="Fecha \n Desde - Hasta", width=223, height=40, fg_color="White", bg_color="White", text_color="Black", font=("Arial", 16,"bold"))
lbl19.grid(row=2, column=2, padx=1, pady=1)

lbl20 = customtkinter.CTkLabel(TablaFinal, text="Dias", **estiloTablaFinal)
lbl20.grid(row=2, column=3, padx=1, pady=1)

lbl21 = customtkinter.CTkLabel(TablaFinal, text="kWh Total", **estiloTablaFinal)
lbl21.grid(row=2, column=4, padx=1, pady=1)

lbl22 = customtkinter.CTkLabel(TablaFinal, text="kWh Total", **estiloTablaFinal)
lbl22.grid(row=2, column=5, padx=1, pady=1)

lbl23 = customtkinter.CTkLabel(TablaFinal, text="kWh Total",  **estiloTablaFinal)
lbl23.grid(row=2, column=6, padx=1, pady=1)

DatosBD = customtkinter.CTkFrame(ventana, width=850, height=265, fg_color="Black", bg_color="Black")
DatosBD.pack_propagate(False)
DatosBD.place(relx=0.43, rely=0.5)

# Apartado para los datos de la BD

style = ttk.Style()
style.configure("Treeview", font=("Arial", 16))

Tabla = ttk.Treeview(DatosBD, columns=("FECHA", "DESDE", "HASTA", "DIAS", "CONSUMO", "CONSUMNO_DF", "CONSUMO_D"), show="tree")
Tabla.column("#0", width=0, stretch=tk.NO)
Tabla.column("FECHA", anchor=CENTER, width=153)
Tabla.column("DESDE", anchor=CENTER, width=76)
Tabla.column("HASTA", anchor=CENTER, width=76)
Tabla.column("DIAS", anchor=CENTER, width=154)
Tabla.column("CONSUMO", anchor=CENTER, width=154)
Tabla.column("CONSUMNO_DF", anchor=CENTER, width=154)
Tabla.column("CONSUMO_D", anchor=CENTER, width=154)

for col in ("FECHA", "DESDE", "HASTA", "DIAS", "CONSUMO", "CONSUMNO_DF", "CONSUMO_D"):
    Tabla.column(col, anchor=tk.CENTER, width=115)
    Tabla.heading(col, text="") 

# Crear Scrollbar
scrollbar = ttk.Scrollbar(DatosBD, orient="vertical", command=Tabla.yview)
Tabla.configure(yscrollcommand=scrollbar.set)

# Posicionar elementos
Tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

TotalBD = customtkinter.CTkFrame(ventana, width=850, height=40, fg_color="Black", bg_color="Black")
TotalBD.place(relx=0.43, rely=0.8)

lblTotal = customtkinter.CTkLabel(TotalBD, text="Total :",  width=344, height=40, fg_color="White", bg_color="White", text_color="Black", font=("Arial", 16,"bold"))
lblTotal.grid(row=1, column=1, padx=1, pady=1)

totalDias = customtkinter.CTkLabel(TotalBD, text="00.0",  **estiloTablaFinal)
totalDias.grid(row=1, column=3, padx=1, pady=1)

totalCFRkwh = customtkinter.CTkLabel(TotalBD, text="00.0",  **estiloTablaFinal)
totalCFRkwh.grid(row=1, column=4, padx=1, pady=1)

totalDFkwh = customtkinter.CTkLabel(TotalBD, text="00.0",  **estiloTablaFinal)
totalDFkwh.grid(row=1, column=5, padx=1, pady=1)

totalDkwh = customtkinter.CTkLabel(TotalBD, text="00.0",  **estiloTablaFinal)
totalDkwh.grid(row=1, column=6, padx=1, pady=1)

DatosFinales = { 
        "fg_color": ("Lightgray"), 
        "bg_color": ("Lightgray"), 
        "text_color": ("Black"), 
        "width": 80, 
        "height": 40, 
        "font": ("Arial", 16, "bold")
}

lbl24 = customtkinter.CTkLabel(ventana, text="Tarifa del servicio :", **DatosFinales)
lbl24.place(relx=0.5, rely=0.85)

lbl25 = customtkinter.CTkLabel(ventana, text="00", **DatosFinales)
lbl25.place(relx=0.585, rely=0.85)

lbl26 = customtkinter.CTkLabel(ventana, text="Suministro en Baja - Baja", **DatosFinales)
lbl26.place(relx=0.63, rely=0.85)

lbl27 = customtkinter.CTkLabel(ventana, text="Recuperacion :", **DatosFinales)
lbl27.place(relx=0.5, rely=0.88)

lbl28 = customtkinter.CTkLabel(ventana, text="0000", **DatosFinales)
lbl28.place(relx=0.58, rely=0.88)

lbl29 = customtkinter.CTkLabel(ventana, text="kWh Totales", **DatosFinales)
lbl29.place(relx=0.63, rely=0.88)

lbl30 = customtkinter.CTkLabel(ventana, text="Periodo del ajuste :", **DatosFinales)
lbl30.place(relx=0.5, rely=0.91)

lbl31 = customtkinter.CTkLabel(ventana, text="", **DatosFinales)
lbl31.place(relx=0.59, rely=0.91)

lbl32 = customtkinter.CTkLabel(ventana, text="Anomalia :", **DatosFinales)
lbl32.place(relx=0.5, rely=0.94)

lbl33 = customtkinter.CTkLabel(ventana, text="-------------------", **DatosFinales)
lbl33.place(relx=0.59, rely=0.94)
  
ventana.mainloop()