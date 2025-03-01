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
import re
import os
from datetime import date

# Carregando a fonte Roboto
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

def mil_pol_mm(mm):
    return mm * 2.83465

# Configuração do PDF
cnv = canvas.Canvas('Contrato.pdf', pagesize=A4)
largura, altura = A4 
nome_contratante = []

# Função de cabeçalho
def cabecalho():
    # Adiciona uma pequena margem na cor azul
    cnv.setFillColor(HexColor("#003f66"))
    cnv.rect(0, altura - 28, 150, 50, stroke=0, fill=1)

    # Adiciona o texto principal com destaque
    cnv.setFillColor(HexColor("#ff4500")) # Define a cor do texto
    cnv.setFont('Roboto-Bold', 35) # Configura a fonte como "Roboto-Bold" (negrito)
    cnv.drawCentredString(148, altura - 75, 'CONTRATO')    
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Bold', 13)
    cnv.drawCentredString(148, altura - 95, 'DE PRESTAÇÃO DE SERVIÇOS')
    
    # Adiciona o texto informaçoes pessoais e logo
    cnv.setFont('Roboto-Bold', 12)
    cnv.drawCentredString(500, altura - 62, 'ANTONIOJRSALES')
    cnv.setFont('Roboto-Regular', 11)
    texto = ' '.join('DEVELOPER')  # 2 espaços
    cnv.drawCentredString(500, altura - 77, texto)
    cnv.drawImage('artificialbrain.png', 410, altura - 82, width=30, height=30, mask='auto')

# Função de rodape
def roda_pe():
    # Adicionando cor de fundo
    cnv.setFillColor(HexColor("#003f66"))
    cnv.rect(0, altura - 840, 600, 50, stroke=0, fill=1)

    # Adiciona o texto informaçoes pessoais
    cnv.setFillColor(colors.white)
    cnv.setFont('Roboto-Regular', 9)
    cnv.drawCentredString(184, altura - 822, 'E-mail: antoniogomes.junio@gmail.com  |  WhatsApp: (85) 99200-6309  |  ')
    cnv.setFont('Roboto-Regular', 9)
    
    # Adiciona o texto do LinkedIn
    cnv.drawString(330, altura - 822, 'LinkedIn: linkedin.com/in/antonio-gomes-31bb18137/')
    
    # Cria o link clicável
    cnv.linkURL('https://linkedin.com/in/antonio-gomes-31bb18137/',(330, altura - 822, 580, altura - 810))

# Função para validar e formatar CPF/CNPJ
def formatar_cpf_cnpj(documento):
    documento = re.sub(r'\D', '', documento)  # Remove caracteres não numéricos
    if len(documento) == 11:
        return f'{documento[:3]}.{documento[3:6]}.{documento[6:9]}-{documento[9:]}'
    elif len(documento) == 14:
        return f'{documento[:2]}.{documento[2:5]}.{documento[5:8]}/{documento[8:12]}-{documento[12:]}'
    else:
        return documento

# Função para coletar dados do contratante
def coletar_dados_contratante():
    # Desenhar o contorno arredondado
    cnv.setLineWidth(1)
    cnv.roundRect(28, altura - 230, mil_pol_mm(180), 90, 10, stroke=1, fill=0)
    cnv.setFillColor(colors.black)
    cnv.drawImage('perfil.png', 28, altura - 137, width=20, height=20, mask='auto')
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(52, altura - 133, 'Contratante:')
    while True:
        nome = input('Digite o seu nome contratante: ').strip()
        nome_contratante.append(nome)
        if not nome or nome.isnumeric():
            print("Erro: O valor de Nome e invalido ou pode estar vazio.")
            continue
        
        nacionalidade = input('Digite o pais que nasceu: ').strip()
        if not nacionalidade or nacionalidade.isnumeric():
            print("Erro: O valor Nacionalidade e invalido ou pode estar vazia.")
            continue
        
        empresa = input('Digite o nome da Empresa: ').strip()
        if not empresa:
            print("Erro: Nome da empresa não pode estar vazio.")
            continue
        
        cpf_cnpj_formatado = "Não informado"  # Valor padrão para evitar erro
        while True:
            cpf_cnpj = input("Digite o CPF ou CNPJ do contratante: ").strip()
            if cpf_cnpj and cpf_cnpj.isdigit():
                if len(cpf_cnpj) == 11 or len(cpf_cnpj) == 14:
                    cpf_cnpj_formatado = formatar_cpf_cnpj(cpf_cnpj)
                    break
                else:
                    print("CPF/CNPJ inválido. Deve conter 11 ou 14 dígitos. Tente novamente.")
            else:
                print("Entrada inválida. Digite apenas números.")

        # Escrever os dados no PDF
        cnv.setFillColor(colors.black)
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(43, altura - 160, f'Nome: {nome.title()}')
        cnv.drawString(43, altura - 178, f'Nacionalidade: {nacionalidade.title()}')
        cnv.drawString(43, altura - 196, f'Empresa: {empresa.title()}')
        cnv.drawString(43, altura - 214, f'CPF / CNPJ: {cpf_cnpj_formatado}')
        break
    return altura - 224

def coletar_dados_prestador():
    cnv.setLineWidth(1)
    cnv.roundRect(28, altura - 350, mil_pol_mm(180), 90, 10, stroke=1, fill=0)
    cnv.drawImage('perfilgradient.png', 28, altura - 257, width=20, height=20, mask='auto')
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(52, altura - 252, 'Prestador de Serviço:')
    nome_prest = 'Antonio Gomes Sales Junior'
    nacionalidade_prest = 'Brasil'
    cpf_prest = 'xxx.xxx.xxx-xx'
    profissao_prest = 'Desenvolvedor'
    
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Regular', 12) # Fonte padrão
    cnv.drawString(43, altura - 280, f'Nome: {nome_prest}')
    cnv.drawString(43, altura - 298, f'Nacionalidade: {nacionalidade_prest}')
    cnv.drawString(43, altura - 316, f'CPF / CNPJ: {cpf_prest}')
    cnv.drawString(43, altura - 334, f'Profissao: {profissao_prest}')
    return altura - 344
    
def clausulas():
    os.system('cls')
    while True:
        ### Clausula 1 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 380, 'CLÁUSULA 1 – DO OBJETO')    
        servico = input('Digite o servico a ser prestado: ').strip()
        if not servico:
            print("Erro: Tipo de serviço não pode estar vazia.")
            continue
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 400, f'O presente contrato tem como objeto a prestação de serviços: ({servico})')
        
        ### Clausula 2 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 425, 'CLÁUSULA 2 – DO VALOR E FORMA DE PAGAMENTO')        
        valor_servico = input('Digite o valor do servico a ser prestado: ').strip()
        if not valor_servico or valor_servico.isalpha():
            print("Erro: O Valor do serviço e invalido ou pode estar vazia.")
            continue
        else:
            valor_servico_float = float(valor_servico)        
        forma_pag = input('Digite a forma de pagamento do servico a ser prestado [Vista, Parcelado, Com vencimentos]: ').strip().lower()
        lista_form_pag = ['vista', 'parcelado', 'com vencimentos']
        if not forma_pag or forma_pag not in lista_form_pag:
            print("Erro: A Forma de pagamento esta fora da lista prevista ou pode estar vazia.")
            continue
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 445, f'O valor total do contrato será de R$ {valor_servico_float:.2f}, que será pago da seguinte forma.')
        cnv.drawString(28, altura - 460, f'Forma de pagamento: {forma_pag.capitalize()}')       

        ### Clausula 3 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 485, 'CLÁUSULA 3 – DO OBJETO')
        prazo_servico = input('Digite quantos dias de servico a ser prestado: ')
        if not prazo_servico or prazo_servico.isalpha():
            print("Erro: A data do serviço e invalido ou pode estar vazia.")
            continue
        data_inicio = input('Digite o dia de inicio do servico: ')
        data_final = input('Digite o dia de finalizacao do servico: ')      
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 505, f'O prazo para a execução dos serviços será de {prazo_servico} dias, com início em {data_inicio} e término em {data_final},')
        cnv.drawString(28, altura - 520, f'podendo ser prorrogado mediante acordo entre as partes.')
        
        ### Clausula 4 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 550, 'CLÁUSULA 4 – DAS OBRIGAÇÕES DO CONTRATADO')
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 570, 'O Contratado se obriga a:')
        cnv.drawString(28, altura - 585, '1° - Prestar os serviços descritos na Cláusula 1 com qualidade e eficiência.')
        cnv.drawString(28, altura - 600, '2° - Cumprir o prazo de execução estabelecido.')
        cnv.drawString(28, altura - 615, '3° - Fornecer relatórios ou resultados periódicos, se necessário.')
        
        ### Clausula 5 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 645, 'CLÁUSULA 5 – DAS OBRIGAÇÕES DO CONTRATANTE')
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 665, 'O Contratante se obriga a:')
        cnv.drawString(28, altura - 680, '1°- Efetuar os pagamentos conforme estabelecido na Cláusula 2')
        cnv.drawString(28, altura - 695, '2°- Disponibilizar informações e materiais necessários para a execução dos serviços.')
        cnv.drawString(28, altura - 710, '3°- Cooperar com o Contratado no que for necessário para a execução do objeto deste contrato.')

        cnv.showPage() # Quebra de página

        ### Clausula 6 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 50, 'CLÁUSULA 6 – DA RESCISÃO')
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 70, 'Este contrato poderá ser rescindido por qualquer uma das partes, mediante aviso prévio de [X dias],') 
        cnv.drawString(28, altura - 85, 'em caso de descumprimento das obrigações aqui estabelecidas. Em caso de rescisão sem justificativa,') 
        cnv.drawString(28, altura - 100, 'a parte que rescindir o contrato deverá pagar uma multa de [valor ou percentual] sobre o valor total do' ) 
        cnv.drawString(28, altura - 115, 'contrato.')

        ### Clausula 7 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 145, 'CLÁUSULA 7 – DA CONFIDENCIALIDADE')
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 165, 'Ambas as partes se comprometem a manter em sigilo todas as informações confidenciais a que tenham, ')
        cnv.drawString(28, altura - 180, 'acesso durante a execução deste contrato, não podendo divulgá-las a terceiros sem prévia autorização.')

        ### Clausula 8 ###
        cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(28, altura - 210, 'CLÁUSULA 8 – DAS DISPOSIÇÕES GERAIS')
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(28, altura - 230, '1°- A tolerância de qualquer das partes quanto ao descumprimento de qualquer obrigação estabelecida neste contrato não implicará em novação ou renúncia de direito.')
        cnv.drawString(28, altura - 245, '2°- Este contrato poderá ser alterado mediante acordo mútuo entre as partes, por escrito.')
        
        roda_pe()
        return altura - 255

def coletar_assinaturas():
    cnv.setFont('Roboto-Bold', 12)
    cnv.setFillColor(HexColor("#000000"))

    cnv.drawString(28, altura - 285, 'Justo e acordado, firmam as partes:')
    cnv.drawImage('aperto-de-mao.png', 240, altura - 300, width=28, height=28, mask='auto')

    # Contratante
    cnv.setFont('Roboto-Bold', 12)
    cnv.setFillColor(HexColor("#00A69C"))
    cnv.drawImage('perfil.png', 28, altura - 340, width=22, height=22, mask='auto')
    cnv.drawString(53, altura - 335, "CONTRATANTE:")
    cnv.setFont('Roboto-Bold', 12)
    cnv.setFillColor(HexColor("#000000"))
    cnv.drawString(28, altura - 355, ''.join(nome_contratante))

    # Contratado
    cnv.setFont('Roboto-Bold', 12)
    cnv.setFillColor(HexColor("#005487"))
    cnv.drawImage('perfilgradient.png', 335, altura - 340, width=22, height=22, mask='auto')
    cnv.drawString(360, altura - 335, "CONTRATADO:")
    cnv.setFont('Roboto-Bold', 12)
    cnv.setFillColor(HexColor("#000000"))
    cnv.drawString(320, altura - 355, "Antonio Gome Sales Junior")

    # Cidade e data
    cnv.setFont('Roboto-Bold', 12)
    cidade = 'Fortaleza'
    data = date.today()
    mes_atual = data.month
    mes = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro',
    }
    mes_atual_extenso = mes[mes_atual]
    
    cnv.drawString(320, altura - 400, f'{cidade}, {data.strftime("%d")} de {mes_atual_extenso} de {data.strftime("%Y")}')

    # Linhas para assinaturas
    cnv.line(100, 330, 250, 330)  # Linha Contratante
    cnv.line(300, 330, 450, 330)  # Linha Contratado

    # Legendas abaixo das linhas
    cnv.setFont("Helvetica-Bold", 8)
    cnv.setFillColor(HexColor("#00A69C"))
    cnv.drawString(130, 300, "Assinatura Contratante")

    cnv.setFillColor(HexColor("#005487"))
    cnv.drawString(330, 300, "Assinatura Contratado")

    cnv.drawImage('assinatura.png', 267, altura - 620, width=40, height=40, mask='auto')

def main():
    cabecalho()
    roda_pe()
    coletar_dados_contratante()
    coletar_dados_prestador()
    clausulas()
    coletar_assinaturas()
    
    cnv.save()

if __name__ == "__main__":
    main()

