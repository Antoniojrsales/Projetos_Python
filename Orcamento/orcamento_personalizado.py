#Bibliotecas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.units import cm
from datetime import date, datetime
import os

# Carregando a fonte Roboto
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

# Configuração do PDF
cnv = canvas.Canvas('Orcamento-personalizado.pdf', pagesize=A4)
largura, altura = A4


def mil_pol_mm(mm):
    return mm * 2.83465

# Função de cabeçalho
def header():
    try:
        cnv.setFillColor(HexColor("#003f66"))
        cnv.rect(0, altura - 28, 150, 50, stroke=0, fill=1)

        print("\n=== INSIRA OS DADOS DO SERVIÇO ===")
        while True:
            servico = input('Digite qual o servico a ser prestado: ').strip()
            if not servico:
                print("Erro: O valor de Nome e invalido ou pode estar vazio.")
                continue
            break
        cnv.setFillColor(HexColor("#ff4500"))
        cnv.setFont('Roboto-Bold', 12)
        cnv.drawCentredString(170, altura - 75, f'{servico}')
        
        # Adicionando data com mês por extenso
        cnv.setFillColor(colors.black)
        cnv.setFont('Roboto-Bold', 12)
        data = date.today()
        meses = {
            1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
            5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
            9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
        }
        mes_atual_extenso = meses[data.month]
        cnv.drawCentredString(95, altura - 95, f'Data: {data.strftime("%d")}/{mes_atual_extenso}/{data.strftime("%Y")}')
        
        # Logotipo
        cnv.setFont('Roboto-Bold', 12)
        cnv.drawCentredString(500, altura - 62, 'ANTONIOJRSALES')
        cnv.setFont('Roboto-Regular', 11)
        cnv.drawCentredString(500, altura - 77, 'DEVELOPER')
        cnv.drawImage('artificialbrain.png', 410, altura - 82, width=30, height=30, mask='auto')
    except FileNotFoundError:
        print("Aviso: Arquivo 'artificialbrain.png' não encontrado.")

# Função de rodape
def footer():
    # Adicionando cor de fundo
    cnv.setFillColor(HexColor("#003f66"))
    cnv.rect(0, altura - 840, 600, 50, stroke=0, fill=1)

    # Adiciona o texto informaçoes pessoais
    cnv.setFillColor(colors.white)
    cnv.setFont('Roboto-Bold', 12)
    cnv.drawCentredString(largura / 2, altura - 822, f'Copyright © 2025 by <AntonioJrSales>. All Rights Reserved.')

def contractor():
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Bold', 15) # Fonte maior e em negrito
    cnv.drawString(40, altura - 150, 'A/C:')
    os.system('cls')
    print("\n=== INSIRA OS DADOS DO CONTRATANTE ===")
    while True:
        nome = input('Digite o seu nome contratante: ').strip()
        if not nome or nome.isnumeric():
            print("Erro: O valor de Nome e invalido ou pode estar vazio.")
            continue

        # Escrever os dados no PDF
        cnv.setFillColor(colors.black)
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(40, altura - 170, f'Nome: {nome.title()}')
        #cnv.drawString(40, altura - 185, f'Telefone: ({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}')
        #cnv.drawString(40, altura - 200, f'Endereço: {rua}, {numero} - {bairro} {cidade}')
        break
    return altura - 220

def criar_perguntas_cliente():
    print("\n=== INSIRA AS PERGUNTAS ===")
    dados = []  # Cabeçalho
    while True:
        perguntas = input("Deseja perguntar oque (ou ENTER para finalizar): ").strip()
        if not perguntas:
            break
        if perguntas in [item[0] for item in dados[1:]]:
            print("Pergunta já adicionada. Tente novamente!")
            continue
        dados.append([perguntas])
    print("\nPerguntas criadas com sucesso")
    #for pergunta in dados[1:]:
        #print(f"- {pergunta[0]}")
    return dados

def desenhar_pergunta(cnv, perguntas, largura_maxima, altura_inicial):
    altura = altura_inicial  # Posição inicial no PDF
    espaco_entre_linhas = 15  # Espaçamento entre as linhas

    def dividir_texto(texto, largura_maxima):
        cnv.setFont('Roboto-Regular', 12)
        if isinstance(texto, list):  # Verifica se é uma lista e converte para string
            texto = " ".join(texto)
        palavras = texto.split(" ")
        linhas = []
        linha_atual = ""

        for palavra in palavras:
            if cnv.stringWidth(linha_atual + palavra + " ") <= largura_maxima:
                linha_atual += palavra + " "
            else:
                linhas.append(linha_atual.strip())
                linha_atual = palavra + " "
        linhas.append(linha_atual.strip())
        return linhas

    for pergunta in perguntas:
        if isinstance(pergunta, list):  # Garantir que `pergunta` seja uma string
            pergunta = " ".join(pergunta)
        linhas = dividir_texto(pergunta, largura_maxima)

        for linha in linhas:
            if altura < 40:  # Verifica limite inferior da página
                cnv.showPage()
                altura = altura_inicial
            cnv.drawString(40, altura, linha)
            altura -= espaco_entre_linhas  # Ajusta altura para a próxima linha

    return altura  # Retorna a altura final para continuar o layout

def info_adicionais():
    cnv.setFont('Roboto-Regular', 12)
    cnv.drawString(40, altura - 400, ' Fico à disposição para discutirmos os detalhes e desenvolver a solução ideal para o seu negócio.')
    cnv.drawString(40, altura - 430, 'Aguardo seu retorno!')
    cnv.drawString(40, altura - 460, 'Atenciosamente,')
    cnv.drawString(40, altura - 475, 'Antonio Gomes')
    cnv.drawString(40, altura - 490, 'Desenvolvedor Python | Automação e Integração de Dados')

def payment_method():
    cnv.setFillColor(HexColor("#ff4500")) # Define a cor do texto
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(40, altura - 540, 'FORMA DE PAGAMENTO')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 12) # Fonte padrão
    #cnv.drawString(40, altura - 555, 'Pix com 10% de desconto ou 2x no cartao de credito')
    
    cnv.setFillColor(HexColor("#ff4500")) # Define a cor do texto
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(40, altura - 580, 'TERMOS E CONDICOES')
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 12) # Fonte padrão
    #cnv.drawString(40, altura - 595, 'Esse orçamento e valido por 30 dias.')

def info_person():
    try:
        cnv.drawImage('whatsapp.png', 345, altura - 550, width=30, height=30, mask='auto')
        cnv.setFillColor(colors.black)
        cnv.setFont('Roboto-Bold', 10)
        cnv.drawString(375, altura - 540, '(85) 99200-6309')

        cnv.drawImage('email.png', 351, altura - 572, width=19, height=19, mask='auto')
        cnv.drawString(375, altura - 567, 'antoniogomes.junio@gmail.com')

        cnv.drawImage('linkedin.png', 348, altura - 602, width=25, height=25, mask='auto')
        cnv.drawString(375, altura - 593, 'linkedin.com/in/antonio-gomes-31bb18137/')

        cnv.drawImage('home.jpeg', 351, altura - 628, width=20, height=20, mask='auto')
        cnv.drawString(375, altura - 622, 'https://antoniojrsales.github.io/meu_portfolio/')
    except FileNotFoundError as e:
        print(f"Aviso: {e}")

def main():
    header()  # Cabeçalho com informações
    footer()  # Rodapé
    contractor()  # Dados do contratante
    #payment_method() # Dados do forma de pagamento
    info_person()
    info_adicionais()
    # Define largura e altura iniciais
    largura_maxima = largura - 90  # Largura útil (com margens)
    altura_inicial = altura - 210

    # Coleta e desenha perguntas
    perguntas = criar_perguntas_cliente()
    desenhar_pergunta(cnv, perguntas, largura_maxima, altura_inicial)
    
    cnv.save()  # Finaliza o canvas


if __name__ == "__main__":
    main()