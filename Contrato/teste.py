#Bibliotecas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
import os

# Carregando a fonte Roboto
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

def mil_pol_mil(mil):
    return mil / 0.35777

def mil_pol_mm(mm):
    return mm * 2.83465

# Configuração do PDF
cnv = canvas.Canvas('contrato_ajustado.pdf', pagesize=A4)
largura, altura = A4 

# Função de cabeçalho
def cabecalho():
    # Fundo azul escuro
    cnv.setFillColor(HexColor("#003f66"))
    cnv.rect(0, altura - mil_pol_mil(10), 150, 50, stroke=0, fill=1)

    # Texto cabecalho (Título)
    cnv.setFillColor(HexColor("#ff4500")) # Define a cor do texto como preta
    cnv.setFont('Roboto-Bold', 32) # Configura a fonte como "Roboto-Bold" (negrito) com tamanho 20
    cnv.drawCentredString(150, altura - mil_pol_mil(28), 'CONTRATO')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Bold', 13)
    cnv.drawCentredString(148, altura - mil_pol_mil(36), 'DE PRESTAÇÃO DE SERVIÇOS')

    cnv.setFont('Roboto-Bold', 12)
    cnv.drawCentredString(500, altura - mil_pol_mil(31), 'ANTONIOJRSALES')

    cnv.setFont('Roboto-Regular', 12)
    cnv.drawCentredString(500, altura - mil_pol_mil(36), 'DEVELOPER')

    # Inicialização de y
y = altura - mil_pol_mil(40)

# Cabeçalho
cabecalho()

cnv.save()