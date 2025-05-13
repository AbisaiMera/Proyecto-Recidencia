from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib import colors
from reportlab.lib.units import mm, inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER, TA_JUSTIFY
from datetime import datetime
import os, platform

def generar_reporte_pdf(nombre, direccion, medidor, tarifa, rpu, anomalia, descripcion, metodo, periodo_ajuste, persona, situacion, cpd_data, rpe, nomrpe):
    doc = SimpleDocTemplate("reporte_ajuste.pdf", pagesize=LETTER,
                            rightMargin=50, leftMargin=50,
                            topMargin=100, bottomMargin=50)

    # Estilos
    styles = getSampleStyleSheet()

    # Estilo base justificado
    style = ParagraphStyle(name="JustifiedBase", parent=styles["Normal"], fontName="Helvetica", fontSize=12, leading=16, alignment=TA_JUSTIFY)

    # Otros estilos
    bold = ParagraphStyle(name="Bold", parent=style, fontName="Helvetica-Bold")
    justified = ParagraphStyle(name="Justified", parent=style, fontName="Helvetica", fontSize=12, leading=16, alignment=TA_JUSTIFY)
    right_green = ParagraphStyle(name="RightGreen", parent=style, fontName="Helvetica-Bold", fontSize=10, alignment=TA_RIGHT, textColor=colors.HexColor("#009640"))

    story = []

    # --- Encabezado alineado a la derecha ---
    story.append(Paragraph("División de Distribución Centro Oriente", right_green))
    story.append(Paragraph("Zona de Distribución Tula", right_green))
    story.append(Paragraph("Departamento de Medición Conexiones y Servicios", right_green))
    story.append(Spacer(1, 6))
    story.append(Paragraph(datetime.now().strftime("%d de %B de %Y"), style))
    story.append(Spacer(1, 20))

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
    story.append(Paragraph(anomalia, style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("MÉTODO DE CÁLCULO DE AJUSTE:", bold))
    story.append(Paragraph(metodo, justified))
    story.append(Spacer(1, 12))

   # Tabla CPD
    story.append(Paragraph("CÁLCULO DE C.P.D.", bold))
    table_data = [["Periodo", "Consumo", "Días", "C.P.D."]] + cpd_data

    # Totales
    total_consumo = sum(int(row[1]) for row in cpd_data)
    total_dias = max(int(row[2]) for row in cpd_data)
    total_cpd = sum(float(row[3]) for row in cpd_data) / len(cpd_data)
    table_data.append(["TOTAL", str(total_consumo), str(total_dias), f"{total_cpd:.4f}"])

    t = Table(table_data, colWidths=[20*mm, 20*mm, 20*mm, 20*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.yellow),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(Spacer(1, 12))
    story.append(t)
    story.append(Spacer(1, 20))

    # Periodo del ajuste
    story.append(Paragraph("PERIODO DEL AJUSTE:", bold))
    story.append(Paragraph(periodo_ajuste, style))
    story.append(Spacer(1, 12))

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

    doc.build(story)

    # Abrir el PDF automáticamente
    pdf_filename = "reporte_ajuste.pdf"
    if platform.system() == "Windows":
        os.startfile(pdf_filename)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {pdf_filename}")
    else:  # Linux y otros
        os.system(f"xdg-open {pdf_filename}")
