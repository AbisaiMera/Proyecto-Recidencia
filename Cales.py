from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle

def generar_pdf(datos):
    archivo_pdf = "Memoria_Tecnica.pdf"
    doc = SimpleDocTemplate(archivo_pdf, pagesize=letter, leftMargin=20, rightMargin=20, topMargin=20, bottomMargin=30)
    styles = getSampleStyleSheet()
    elementos = []
    
   # Agregar imagen del encabezado en la esquina superior izquierda
    imagen_encabezado = Image("Logo_CFE.png", width=150, height=40)
    tabla_encabezado = Table([[imagen_encabezado]], colWidths=[575])
    tabla_encabezado.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('VALIGN', (0, 0), (0, 0), 'TOP')
    ]))
    elementos.append(tabla_encabezado)
    elementos.append(Spacer(1, 20))
    
    # Estilo para el título
    estilo_titulo = ParagraphStyle(name="Titulo", alignment=1, fontSize=14, spaceAfter=12, bold=True)
    titulo = Paragraph("MEMORIA TÉCNICA PARA DETERMINAR AJUSTE A LA FACTURACIÓN", estilo_titulo)
    elementos.append(titulo)
    elementos.append(Spacer(1, 20))
    
    # Tabla para datos generales con formato
    data = [[f"<b>{key}:</b> {value}"] for key, value in datos.items() if key not in ["Descripción de la Anomalía"]]
    tabla = Table(data, colWidths=[450])
    tabla.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5)
    ]))
    elementos.append(tabla)
    elementos.append(Spacer(1, 20))
    
    # Descripción de la anomalía con estilo
    estilo_subtitulo = ParagraphStyle(name="Subtitulo", fontSize=12, bold=True, spaceAfter=6)
    estilo_texto = ParagraphStyle(name="Texto", fontSize=11, leading=14)
    
    elementos.append(Paragraph("DESCRIPCIÓN DE LA ANOMALÍA:", estilo_subtitulo))
    elementos.append(Paragraph(datos["Descripción de la Anomalía"], estilo_texto))
    
    # Guardar el PDF
    doc.build(elementos)
    print(f"PDF generado correctamente: {archivo_pdf}")
    
# Datos de prueba (reemplazar con valores dinámicos de Tkinter)
datos = {
    "Nombre": "Vinicio Valzquez B",
    "Dirección": "C INSURG #1 DOM",
    "Medidor": "18K6C6",
    "Tarifa": "01",
    "R.P.U.": "272991000151",
    "Descripción de la Anomalía": "Dando cumplimiento al programa de revisión de servicios en baja tensión nos constituimos en el domicilio ...",
    "Tipo de Giro": "Casa habitación",
    "Método de Cálculo": "Historial de consumo.",
    "Periodo del Ajuste": "09 de septiembre de 2019 - 02 de enero de 2025",
    "Situación Actual": "Suspensión del servicio."
}

generar_pdf(datos)
