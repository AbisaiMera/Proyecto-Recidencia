from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import Image, Table, TableStyle, Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.utils import ImageReader
from datetime import datetime
import os, platform
import html
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from io import BytesIO
from reportlab.platypus import Image

def generar_grafica(fechas_int, consumo, consumo_df):
    fig, ax = plt.subplots(figsize=(8, 4.5))

    # Convertimos fechas a enteros por si acaso
    fechas_int = list(map(int, fechas_int))

    # Creamos índices uniformes para el eje X
    x_vals = list(range(len(fechas_int)))

    # Graficamos usando índices para una separación visual uniforme
    ax.plot(x_vals, consumo, label='Facturó', color='cornflowerblue', marker='o')
    ax.plot(x_vals, consumo_df, label='Debió Facturar', color='darkorange', marker='o')

    ax.set_xlabel('Fecha')
    ax.set_ylabel('Consumo')
    ax.grid(axis='y', linestyle='--', linewidth=0.5)

    # Asignamos las fechas originales como etiquetas del eje X
    ax.set_xticks(x_vals)
    ax.set_xticklabels(fechas_int, rotation=45)

    ax.legend(loc='lower left')
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=150)
    buffer.seek(0)
    plt.close(fig)
    return buffer


def agregar_encabezado(canvas, doc):
    canvas.saveState()

    # Ruta al logo
    logo_path = "Imagenes/Logo_CFE.png"
    logo = ImageReader(logo_path)

    # Coordenadas absolutas para el logo (desde esquina inferior izquierda)
    canvas.drawImage(logo, x=doc.leftMargin, y=LETTER[1] - 70, width=200, height=80, preserveAspectRatio=True)

    # Líneas alineadas a la derecha
    right_x = LETTER[0] - doc.rightMargin
    top_y = LETTER[1] - 30  # Ajusta para moverlo más arriba o abajo

    canvas.setFont("Helvetica-Bold", 11)
    canvas.setFillColor(colors.HexColor("#009640"))
    canvas.drawRightString(right_x, top_y, "División de Distribución Centro Oriente")
    canvas.drawRightString(right_x, top_y - 12, "Zona de Distribución Tula")
    canvas.drawRightString(right_x, top_y - 24, "Departamento de Medición Conexiones y Servicios")

    canvas.restoreState()

def construir_tabla_pdf(tipo_tabla, datos):

    if tipo_tabla == "HISTORIAL":
        encabezado = ["Periodo", "Consumo", "Días", "C.P.D."]
        table_data = [encabezado] + datos

        total_consumo = sum(int(row[1]) for row in datos)
        total_dias = max(int(row[2]) for row in datos)
        total_cpd = sum(float(row[3]) for row in datos) / len(datos)

        table_data.append(["TOTAL", str(total_consumo), str(total_dias), f"{total_cpd:.4f}"])

    elif tipo_tabla == "CARGA":
        # Ya viene con encabezado y totales incluidos
        table_data = datos

    elif tipo_tabla == "FACTOR":

        table_data = datos

    else:
        raise ValueError(f"Tipo de tabla no reconocido: {tipo_tabla}")
    
    # ✅ Validar consistencia de filas
    num_cols = len(table_data[0])
    table_data_limpia = []

    for i, fila in enumerate(table_data):
        if not isinstance(fila, list):
            raise ValueError(f"Fila en posición {i} no es una lista: {fila}")
        if len(fila) != num_cols:
            raise ValueError(
                f"Fila {i} tiene {len(fila)} columnas, se esperaban {num_cols}: {fila}"
            )
        table_data_limpia.append([str(cell) for cell in fila])

    # ✅ Ahora sí se puede construir la tabla con seguridad
    tabla_pdf = Table(table_data_limpia, colWidths=[30 * mm] * num_cols)
    tabla_pdf.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.yellow),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),           
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))

    return tabla_pdf

def generar_reporte_pdf(nombre, direccion, medidor, tarifa, rpu, anomalia_texto,
                        descripcion, metodo, giro, periodo_ajuste, persona,
                        situacion, cpd_data, tipo_tabla, rpe, nomrpe, filepath,
                        valor_factor_ajuste=None, explicacion_extra="", incluir_grafica=False,
                        fechas=None, consumos=None, consumos_df=None):
    
    doc = SimpleDocTemplate(filepath, pagesize=LETTER,
                            rightMargin=25, leftMargin=25,
                            topMargin=55, bottomMargin=50)
    
    descripcion = html.escape(descripcion)
    giro = html.escape(giro)
    metodo = html.escape(metodo)
    periodo_ajuste = html.escape(periodo_ajuste)
    persona = html.escape(persona)
    situacion = html.escape(situacion)
    explicacion_extra = html.escape(explicacion_extra or "")

    # Estilos
    styles = getSampleStyleSheet()

    # Estilo base justificado
    style = ParagraphStyle(name="JustifiedBase", parent=styles["Normal"], fontName="Helvetica", fontSize=12, leading=16, alignment=TA_JUSTIFY)

    # Otros estilos
    bold = ParagraphStyle(name="Bold", parent=style, fontName="Helvetica-Bold")
    justified = ParagraphStyle(name="Justified", parent=style, fontName="Helvetica", fontSize=12, leading=16, alignment=TA_JUSTIFY)
    date = ParagraphStyle(name="RightDate", parent=styles["Normal"], fontName="Helvetica", fontSize=12, leading=16, alignment=TA_RIGHT)

    story = []

    story.append(Spacer(1, 12))  # Espacio bajo el encabezado dibujado
    story.append(Paragraph(datetime.now().strftime("%d de %B de %Y"), date))
    story.append(Spacer(1, 20))  # Espacio antes del título u otro contenido


    # --- Título ---
    titulo = ParagraphStyle(name="Titulo", fontName="Helvetica-Bold", fontSize=12, alignment=TA_CENTER)
    story.append(Paragraph("MEMORIA TÉCNICA PARA DETERMINAR AJUSTE A LA FACTURACIÓN", titulo))
    story.append(Spacer(1, 20))

    # --- Datos generales ---
    story.append(Paragraph(f"NOMBRE: {nombre}", bold))
    story.append(Paragraph(f"DIRECCIÓN: {direccion}", bold))
    story.append(Paragraph(f"MEDIDOR: {medidor}", bold))
    story.append(Paragraph(f"TARIFA: {tarifa}", bold))
    story.append(Paragraph(f"R.P.U.: {rpu}", bold))
    story.append(Spacer(1, 20))

    # --- Descripción ---
    story.append(Paragraph("DESCRIPCIÓN DE LA ANOMALÍA:", bold))
    story.append(Paragraph(descripcion, justified))
    story.append(Spacer(1, 12))

    # --- Anomalía y método ---
    story.append(Paragraph("TIPO DE ANOMALÍA:", bold))
    story.append(Paragraph(anomalia_texto, style))
    story.append(Spacer(1, 12))

    # --- Giro ---
    story.append(Paragraph("TIPO DE GIRO:", bold))
    story.append(Paragraph(giro, justified))
    story.append(Spacer(1, 12))

    story.append(Paragraph("MÉTODO DE CÁLCULO DE AJUSTE:", bold))
    story.append(Paragraph(metodo, justified))
    story.append(Spacer(1, 12))

 # --- Tabla dinámica dependiendo del tipo ---
    tabla = construir_tabla_pdf(tipo_tabla, cpd_data)
    story.append(tabla)
    story.append(Spacer(1, 20))

    if tipo_tabla == "FACTOR":
        # Texto inferior (usuario lo escribe)
        story.append(Paragraph(explicacion_extra, justified))
        story.append(Spacer(1, 12))

        # Tabla final con valor del factor
        tabla_final = Table(
            [["FACTOR DE AJUSTE", valor_factor_ajuste]],
            colWidths=[200, 100],
            hAlign='CENTER'
        )
        tabla_final.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.yellow),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        story.append(tabla_final)
        story.append(Spacer(1, 20))

    # Periodo del ajuste
    story.append(Paragraph("PERIODO DEL AJUSTE:", bold))
    story.append(Paragraph(periodo_ajuste, style))
    story.append(Spacer(1, 12))

    if incluir_grafica:
        grafica_buffer = generar_grafica(fechas, consumos, consumos_df)
        imagen_grafica = Image(grafica_buffer, width=500, height=300)
        story.append(Spacer(1, 12))
        story.append(imagen_grafica)

    # Persona que atiende
    story.append(Paragraph("PERSONA QUE ATIENDE REVISIÓN:", bold))
    story.append(Paragraph(persona, style))
    story.append(Spacer(1, 12))

    # Situación actual    
    story.append(Paragraph("SITUACIÓN ACTUAL DEL SERVICIO:", bold))
    story.append(Paragraph(situacion, style))
    story.append(Spacer(1, 30))

    # Firma
    story.append(Paragraph("Atentamente", style))
    story.append(Spacer(1, 30))
    story.append(Paragraph(f"Ing. {nomrpe}", style))
    story.append(Paragraph("Jefe oficina medición Tula.", style))
    story.append(Paragraph(f"R.P.E.: {rpe}", style))

    doc.build(story, onFirstPage=agregar_encabezado, onLaterPages=agregar_encabezado)

     # Abrir PDF
    if platform.system() == "Windows":
        os.startfile(filepath)
    elif platform.system() == "Darwin":
        os.system(f"open '{filepath}'")
    else:
        os.system(f"xdg-open '{filepath}'")
