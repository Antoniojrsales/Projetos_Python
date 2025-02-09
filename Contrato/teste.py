#Bibliotecas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
import os

# Carregando a fonte Roboto
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

def gerar_contrato_pdf(nome, cpf_cnpj, endereco, clausulas):
    pdf_nome = f"Contrato_{nome.replace(' ', '_')}.pdf"
    c = canvas.Canvas(pdf_nome, pagesize=A4)
    largura, altura = A4

    # Fundo azul escuro
    c.setFillColor(HexColor("#003f66"))
    c.rect(0, altura - 1 * cm, 150, 50, stroke=0, fill=1)
    
    # Cabeçalho do contrato
    c.setFillColor(HexColor("#ff4500")) # Define a cor do texto
    c.setFont('Roboto-Bold', 32) # Configura a fonte como "Roboto-Bold" (negrito) com tamanho 20
    c.drawCentredString(largura / 2, altura - 2 * cm, "CONTRATO")
    c.setFillColor(colors.black)
    
    c.setFont('Roboto-Bold', 13)
    c.drawCentredString(148, altura - mil_pol_mil(36), 'DE PRESTAÇÃO DE SERVIÇOS')
    c.setFont('Roboto-Bold', 12)
    c.drawCentredString(500, altura - mil_pol_mil(31), 'ANTONIOJRSALES'
    c.setFont('Roboto-Regular', 12)
    c.drawCentredString(500, altura - mil_pol_mil(36), 'DEVELOPER')