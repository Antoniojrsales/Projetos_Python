# Importando Bibliotecas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import date
import re
import os

# Centralização de configurações
CONFIG = {
    "font_bold": "Helvetica-Bold",
    "font_regular": "Helvetica",
    "header_color": "#003f66",
    "highlight_color": "#ff4500",
    "footer_text_color": colors.white,
    "default_margin": 50,
}

# Configuração do PDF
cnv = canvas.Canvas('Orcamento.pdf', pagesize=A4)
largura, altura = A4


def mil_pol_mm(mm):
    return mm * 2.83465

# Funções auxiliares
def validar_telefone(telefone):
    """Valida formato do telefone (XX)XXXXX-XXXX."""
    return re.fullmatch(r"\(\d{2}\)\d{5}-\d{4}", telefone) is not None

# Função de cabeçalho
def header():
    # Adiciona uma pequena margem na cor azul
    cnv.setFillColor(CONFIG["header_color"])
    cnv.rect(0, altura - 28, 150, 50, stroke=0, fill=1)

    # Adiciona o texto principal com destaque
    cnv.setFillColor(HexColor(CONFIG["highlight_color"])) # Define a cor do texto
    cnv.setFont(CONFIG["font_bold"], 25) # Configura a fonte como "Roboto-Bold" (negrito)
    while True:
        orcamento = input('Digite o numero do Orçamento: ')
        if orcamento.isdigit():
            break
        else:
            print('Favor digitar uma valor valido')
    cnv.drawCentredString(148, altura - 75, f'ORÇAMENTO #{orcamento}')    
    cnv.setFillColor(colors.black)
    cnv.setFont(CONFIG["font_regular"], 12)
    data = date.today()
    mes_atual = data.month
    mes = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro',
    }
    mes_atual_extenso = mes[mes_atual]
    cnv.drawCentredString(103, altura - 95, f'Data: {data.strftime("%d")}/{mes_atual_extenso}/{data.strftime("%Y")}')
    
    # Adiciona o texto informaçoes pessoais e logo
    cnv.setFont(CONFIG["font_regular"], 12)
    cnv.drawCentredString(500, altura - 62, 'ANTONIOJRSALES')
    cnv.setFont(CONFIG["font_regular"], 12)
    texto = ' '.join('DEVELOPER')  # 2 espaços
    cnv.drawCentredString(500, altura - 77, texto)
    cnv.drawImage('artificialbrain.png', 410, altura - 82, width=30, height=30, mask='auto')

# Função de rodape
def footer():
    # Adicionando cor de fundo
    cnv.setFillColor(CONFIG["header_color"])
    cnv.rect(0, altura - 840, 600, 50, stroke=0, fill=1)

    # Adiciona o texto informaçoes pessoais
    cnv.setFillColor(colors.white)
    cnv.setFont(CONFIG["font_regular"], 10)
    cnv.drawCentredString(largura / 2, altura - 822, f'Copyright © 2025 by <AntonioJrSales>. All Rights Reserved.')

def get_contractor_info():
    cnv.setFillColor(colors.black)
    cnv.setFont(CONFIG["font_bold"], 12) # Fonte maior e em negrito
    cnv.drawString(CONFIG["default_margin"], altura - 150, 'A/C:')
    os.system('cls')

    print("\n=== INSIRA OS DADOS DO CONTRATANTE ===")
    while True:
        nome = input("Nome: ").strip()
        if not nome:
            print("Erro: Nome não pode estar vazio.")
            continue

        telefone = input("Telefone (XX)XXXXX-XXXX: ").strip()
        if not validar_telefone(telefone):
            print("Erro: Telefone inválido.")
            continue

        endereco = input("Endereço (Rua, Número, Bairro, Cidade): ").strip()
        if not endereco:
            print("Erro: Endereço não pode estar vazio.")
            continue

        # Escrever os dados no PDF
        cnv.setFillColor(colors.black)
        cnv.setFont(CONFIG["font_regular"], 12) # Fonte padrão
        cnv.drawString(CONFIG["default_margin"], altura - 170, f'Nome: {nome.title()}')
        cnv.drawString(CONFIG["default_margin"], altura - 185, f'Telefone: {telefone}')
        cnv.drawString(CONFIG["default_margin"], altura - 200, f'Endereço: {endereco}')
        break

def criar_dados_tabela():
    print("\n=== INSIRA OS DADOS DOS SERVIÇOS ===")
    dados = [["SERVIÇO", "DESCRIÇÃO", "VALOR"]]  # Cabeçalho
    while True:
        servico = input("Serviço (ou ENTER para finalizar): ").strip()
        if not servico:
            break
        descricao = input("Descrição: ").strip()
        valor = input("Valor: ").strip()
        dados.append([servico, descricao, valor])
    return dados

def desenhar_tabela(cnv, altura_inicial):
    dados = criar_dados_tabela()
    largura_colunas = [200, 250, 90]  # Larguras das colunas
    x_inicial = CONFIG["default_margin"]
    y_atual = altura_inicial
    altura_linha = 15  # Altura de cada linha

    # Função para dividir texto longo em múltiplas linhas
    def dividir_texto(texto, largura_maxima, tamanho_fonte):
        cnv.setFont(CONFIG["font_regular"], tamanho_fonte)
        palavras = texto.split(" ")
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            if cnv.stringWidth(linha_atual + palavra + " ") < largura_maxima:
                linha_atual += palavra + " "
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra + " "
        linhas.append(linha_atual.strip())
        return linhas

    # Desenhar o cabeçalho
    cnv.setFont(CONFIG["font_bold"], 12)
    cnv.setFillColor(HexColor(CONFIG["header_color"]))
    for i, valor in enumerate(dados[0]):
        cnv.drawString(x_inicial + sum(largura_colunas[:i]), y_atual, valor)
    y_atual -= altura_linha

    # Desenhar as linhas da tabela
    cnv.setFont(CONFIG["font_regular"], 10)
    cnv.setFillColor(colors.black)
    for linha in dados[1:]:
        altura_linha_atual = altura_linha
        for i, valor in enumerate(linha):
            largura_coluna = largura_colunas[i]
            texto_quebrado = dividir_texto(valor, largura_coluna, 10)
            for sublinha in texto_quebrado:
                cnv.drawString(x_inicial + sum(largura_colunas[:i]), y_atual, sublinha)
                y_atual -= altura_linha
                altura_linha_atual = max(altura_linha_atual, altura_linha * len(texto_quebrado))
        y_atual -= altura_linha

    return y_atual

def payment_method():
    cnv.setFillColor(HexColor("#ff4500")) # Define a cor do texto
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(55, altura - 540, 'FORMA DE PAGAMENTO')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 12) # Fonte padrão
    cnv.drawString(55, altura - 555, 'Pix com 10% de desconto ou 2x no cartao de credito')
    
    cnv.setFillColor(HexColor("#ff4500")) # Define a cor do texto
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(55, altura - 580, 'TERMOS E CONDICOES')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 12) # Fonte padrão
    cnv.drawString(55, altura - 595, 'Esse orçamento e valido por 30 dias.')

def info_person():
    cnv.drawImage('whatsapp.png', 345, altura - 550, width=30, height=30, mask='auto')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 12) # Fonte padrão
    cnv.drawString(375, altura - 540, '(85) 99200-6309')

    cnv.drawImage('email.png', 351, altura - 572, width=19, height=19, mask='auto')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 11) # Fonte padrão
    cnv.drawString(375, altura - 567, 'antoniogomes.junio@gmail.com')

    cnv.drawImage('linkedin.png', 348, altura - 602, width=25, height=25, mask='auto')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 10) # Fonte padrão
    cnv.drawString(375, altura - 593, 'linkedin.com/in/antonio-gomes-31bb18137/')

    cnv.drawImage('home.jpeg', 351, altura - 628, width=20, height=20, mask='auto')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 10) # Fonte padrão
    cnv.drawString(375, altura - 622, 'https://antoniojrsales.github.io/meu_portfolio/')


def main():
    header()  # Cabeçalho com informações
    footer()  # Rodapé
    get_contractor_info()  # Dados do contratante
    #payment_method() # Dados do forma de pagamento
    #info_person()
    desenhar_tabela(cnv, altura - 280)  # Altura ajustada para a tabela
    
    cnv.save()  # Finaliza o canvas


if __name__ == "__main__":
    main()