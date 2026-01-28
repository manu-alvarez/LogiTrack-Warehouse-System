#!/usr/bin/env python3
"""
LogiTrack Presentation PDF Generator
Creates a 2-page professional PDF presentation
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
import os

# Configuration
ARTIFACTS_DIR = "/Users/manu/.gemini/antigravity/brain/a11ea222-e1b6-4c62-bb45-254407a6117d"
OUTPUT_PATH = "/Users/manu/Desktop/LogiTrack/LogiTrack_Presentacion_Rapida.pdf"

# Colors
PRIMARY_BLUE = HexColor('#0079BF')
DARK_BLUE = HexColor('#172B4D')
LIGHT_GRAY = HexColor('#F4F5F7')
WHITE = HexColor('#FFFFFF')
RED = HexColor('#EB5A46')
GREEN = HexColor('#61BD4F')
ORANGE = HexColor('#F2D600')

def create_pdf():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=A4)
    width, height = A4
    
    # ============= PAGE 1: El Sistema Visual =============
    
    # Background
    c.setFillColor(LIGHT_GRAY)
    c.rect(0, 0, width, height, fill=True)
    
    # Header bar
    c.setFillColor(PRIMARY_BLUE)
    c.rect(0, height - 3*cm, width, 3*cm, fill=True)
    
    # Title
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width/2, height - 2.2*cm, "LogiTrack: Control Total de Almacén")
    
    # Panoramic image
    panoramic_path = os.path.join(ARTIFACTS_DIR, "board_panoramic_1769620474259.png")
    if os.path.exists(panoramic_path):
        img = Image.open(panoramic_path)
        img_width, img_height = img.size
        aspect = img_width / img_height
        
        display_width = width - 2*cm
        display_height = display_width / aspect
        if display_height > 10*cm:
            display_height = 10*cm
            display_width = display_height * aspect
        
        x_pos = (width - display_width) / 2
        y_pos = height - 4*cm - display_height
        
        # Shadow effect
        c.setFillColor(HexColor('#00000033'))
        c.rect(x_pos + 0.2*cm, y_pos - 0.2*cm, display_width, display_height, fill=True)
        
        # Border
        c.setFillColor(WHITE)
        c.rect(x_pos - 0.1*cm, y_pos - 0.1*cm, display_width + 0.2*cm, display_height + 0.2*cm, fill=True)
        
        c.drawImage(panoramic_path, x_pos, y_pos, width=display_width, height=display_height)
    
    # Info boxes - positioned below the image
    box_y = 7*cm
    box_width = 5.5*cm
    box_height = 5*cm
    margin = 1*cm
    
    boxes = [
        {
            'title': '🚦 Colores (Semáforo)',
            'text': 'Rojo para lo urgente,\nverde para lo listo.\nIdentifica prioridades\nal instante.',
            'color': RED
        },
        {
            'title': '➡️ Flujo Claro',
            'text': 'De izquierda a derecha,\nsin saltos ni dudas.\nCada pedido avanza\npor 7 etapas.',
            'color': PRIMARY_BLUE
        },
        {
            'title': '🚚 Transporte',
            'text': 'Identificamos agencias\n(DHL/SEUR) al primer\nvistazo con etiquetas\nde color.',
            'color': ORANGE
        }
    ]
    
    start_x = margin
    for i, box in enumerate(boxes):
        x = start_x + i * (box_width + 0.5*cm)
        
        # Box background
        c.setFillColor(WHITE)
        c.roundRect(x, box_y, box_width, box_height, 0.3*cm, fill=True)
        
        # Color strip
        c.setFillColor(box['color'])
        c.rect(x, box_y + box_height - 0.8*cm, box_width, 0.8*cm, fill=True)
        
        # Title
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(x + box_width/2, box_y + box_height - 0.55*cm, box['title'])
        
        # Text
        c.setFillColor(DARK_BLUE)
        c.setFont("Helvetica", 10)
        lines = box['text'].split('\n')
        for j, line in enumerate(lines):
            c.drawCentredString(x + box_width/2, box_y + box_height - 1.5*cm - j*0.5*cm, line)
    
    # Footer
    c.setFillColor(DARK_BLUE)
    c.setFont("Helvetica", 9)
    c.drawCentredString(width/2, 1*cm, "LogiTrack - Sistema de Gestión de Almacén | Página 1 de 2")
    
    c.showPage()
    
    # ============= PAGE 2: Gestión de Crisis y Orden =============
    
    # Background
    c.setFillColor(LIGHT_GRAY)
    c.rect(0, 0, width, height, fill=True)
    
    # Header
    c.setFillColor(PRIMARY_BLUE)
    c.rect(0, height - 2.5*cm, width, 2.5*cm, fill=True)
    
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - 1.8*cm, "Gestión de Crisis y Orden")
    
    # Section 1: Checklist
    section1_y = height - 4*cm
    
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*cm, section1_y, "✅ Control de Pasos: Nadie olvida el albarán")
    
    checklist_path = os.path.join(ARTIFACTS_DIR, "card_checklist_1769620493158.png")
    if os.path.exists(checklist_path):
        img = Image.open(checklist_path)
        img_width, img_height = img.size
        aspect = img_width / img_height
        
        display_width = width - 3*cm
        display_height = display_width / aspect
        if display_height > 8.5*cm:
            display_height = 8.5*cm
            display_width = display_height * aspect
        
        x_pos = (width - display_width) / 2
        y_pos = section1_y - display_height - 0.5*cm
        
        c.setFillColor(WHITE)
        c.roundRect(x_pos - 0.2*cm, y_pos - 0.2*cm, display_width + 0.4*cm, display_height + 0.4*cm, 0.2*cm, fill=True)
        c.drawImage(checklist_path, x_pos, y_pos, width=display_width, height=display_height)
    
    # Section 2: Incidencias
    section2_y = 12*cm
    
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*cm, section2_y, "⚠️ Gestión de Problemas: Cero papeles perdidos")
    
    incidencia_path = os.path.join(ARTIFACTS_DIR, "card_incidencia_1769620528916.png")
    if os.path.exists(incidencia_path):
        img = Image.open(incidencia_path)
        img_width, img_height = img.size
        aspect = img_width / img_height
        
        display_width = width - 3*cm
        display_height = display_width / aspect
        if display_height > 8.5*cm:
            display_height = 8.5*cm
            display_width = display_height * aspect
        
        x_pos = (width - display_width) / 2
        y_pos = section2_y - display_height - 0.5*cm
        
        c.setFillColor(WHITE)
        c.roundRect(x_pos - 0.2*cm, y_pos - 0.2*cm, display_width + 0.4*cm, display_height + 0.4*cm, 0.2*cm, fill=True)
        c.drawImage(incidencia_path, x_pos, y_pos, width=display_width, height=display_height)
    
    # Footer
    c.setFillColor(DARK_BLUE)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(width/2, 1.5*cm, "Diseñado por Manu Alvarez")
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(width/2, 0.8*cm, "Un sistema que habla solo")
    
    c.save()
    print(f"PDF created: {OUTPUT_PATH}")

if __name__ == "__main__":
    create_pdf()
