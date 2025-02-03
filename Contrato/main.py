from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Carregando a fonte Roboto
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

def configurar_pdf(nome_arquivo):
    # Configura o PDF e define o tamanho da página
    pdf = canvas.Canvas(nome_arquivo, pagesize=A4)
    largura, altura = A4

    # Define margens
    margem_inferior = 2 * cm
    margem_superior = altura - 2 * cm
    margem_esquerda_titulo = 4 * cm
    margem_esquerda = 2 * cm
    margem_direita = largura - 2 * cm

    # Retorna o objeto Canvas e as margens
    return pdf, margem_superior, margem_inferior, margem_esquerda, margem_direita, margem_esquerda_titulo

def adicionar_texto(pdf, texto, x, y, espaco_entre_linhas=14):
    # Adiciona texto com espaçamento ajustável entre linhas
    linhas = texto.split("\n")
    for linha in linhas:
        pdf.drawString(x, y, linha)
        y -= espaco_entre_linhas
    return y

def criar_contrato():
    # Configurações iniciais
    pdf, margem_superior, margem_inferior, margem_esquerda, margem_direita, margem_esquerda_titulo = configurar_pdf("contrato_ajustado.pdf")

    # Posiciona o título
    titulo = "CONTRATO DE PRESTAÇÃO DE SERVIÇOS"
    pdf.setFont("Roboto-Bold", 20)
    y = margem_superior
    y = adicionar_texto(pdf, titulo, margem_esquerda_titulo, y, espaco_entre_linhas=20)

    sub_titulo = "Pelo presente instrumento particular de prestação de serviços"
    pdf.setFont("Roboto-Regular", 12)
    y = margem_superior - 1 * cm
    y = adicionar_texto(pdf, sub_titulo, margem_esquerda, y, espaco_entre_linhas=20)

    # Finaliza o PDF
    pdf.save()

if __name__ == "__main__":
    criar_contrato()