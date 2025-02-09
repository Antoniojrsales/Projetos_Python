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

# Carregando a fonte Roboto
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Regular', 'Roboto-Regular.ttf'))

def mil_pol_mm(mm):
    return mm * 2.83465

# Configuração do PDF
cnv = canvas.Canvas('Contrato.pdf', pagesize=A4)
largura, altura = A4 

# Função de cabeçalho
def cabecalho():
    # Fundo azul escuro
    cnv.setFillColor(HexColor("#003f66"))
    cnv.rect(0, altura - 28, 150, 50, stroke=0, fill=1)

    # Texto cabecalho (Título)
    cnv.setFillColor(HexColor("#ff4500")) # Define a cor do texto
    cnv.setFont('Roboto-Bold', 32) # Configura a fonte como "Roboto-Bold" (negrito) com tamanho 20
    cnv.drawCentredString(150, altura - 75, 'CONTRATO')
    
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Bold', 13)
    cnv.drawCentredString(148, altura - 95, 'DE PRESTAÇÃO DE SERVIÇOS')
    cnv.setFont('Roboto-Bold', 12)
    cnv.drawCentredString(500, altura - 81, 'ANTONIOJRSALES')
    cnv.setFont('Roboto-Regular', 12)
    cnv.drawCentredString(500, altura - 95, 'DEVELOPER')

def roda_pe():
    cnv.setFillColor(HexColor("#003f66"))
    cnv.rect(0, altura - 840, 600, 50, stroke=0, fill=1)

    cnv.setFillColor(colors.white)
    cnv.setFont('Roboto-Regular', 12)
    cnv.drawCentredString(480, altura - 822, 'antoniogomes.junior@gmail.com')

# Função para validar e formatar CPF/CNPJ
def formatar_cpf_cnpj(documento):
    documento = re.sub(r'\D', '', documento)  # Remove caracteres não numéricos
    if len(documento) == 11:
        return f'{documento[:3]}.{documento[3:6]}.{documento[6:9]}-{documento[9:]}'
    elif len(documento) == 14:
        return f'{documento[:2]}.{documento[2:5]}.{documento[5:8]}/{documento[8:12]}-{documento[12:]}'
    else:
        return None

def coletar_dados_contratante():
    # Desenhar o contorno arredondado
    cnv.setLineWidth(1)
    cnv.roundRect(28, altura - 230, mil_pol_mm(180), 90, 10, stroke=1, fill=0)
    cnv.setFillColor(colors.black)
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(43, altura - 135, 'Contratante:')
    while True:
        nome = input('Digite o seu nome contratante: ').strip()
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
        
        cpf_cnpj = input("Digite o CPF ou CNPJ do contratante: ")
        if cpf_cnpj or not cpf_cnpj.isdigit():
            cpf_cnpj_formatado = formatar_cpf_cnpj(cpf_cnpj)
        else:
            print("CPF/CNPJ inválido. Tente novamente.")

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
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(43, altura - 255, 'Prestador de Serviço:')
    nome_prest = 'Antonio Gomes Sales Junior'
    nacionalidade_prest = 'Brasil'
    cpf_prest = '217.884.488-02'
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
        prazo_servico = input('Digite a data da entrega do servico a ser prestado: ')
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
    # Assinaturas
    cnv.line(4 * cm, 3 * cm, 10 * cm, 3 * cm)
    cnv.drawString(mil_pol_mm(0), altura - 354, "Contratante")
    
    cnv.line(12 * cm, 3 * cm, 18 * cm, 3 * cm)
    cnv.drawString(mil_pol_mm(100), altura - 354, "Contratado")

def main():
    cabecalho()
    roda_pe()
    coletar_dados_contratante()
    coletar_dados_prestador()
    clausulas()
    coletar_assinaturas()

if __name__ == "__main__":
    main()

cnv.save()