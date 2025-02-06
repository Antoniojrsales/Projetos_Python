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
cnv = canvas.Canvas('Contrato.pdf', pagesize=A4)
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
      
# Adicionar linhas divisórias
def divisoria(y):
    cnv.setStrokeColor(colors.black)
    cnv.line(mil_pol_mil(10), y, largura - mil_pol_mil(10), y)

def contratante(y):
    # Desenhar o contorno arredondado
    cnv.setLineWidth(1)
    cnv.roundRect(mil_pol_mm(10), y - 145, mil_pol_mm(180), 90, 10, stroke=1, fill=0)
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(mil_pol_mm(15), y - 48, 'Contratante:')
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
        
        cpf_cnpj = input('Digite o seu CPF com 11 digitos / CNPJ com 14 digitos: ').strip()
        if not cpf_cnpj.isdigit() or len(cpf_cnpj) not in [11, 14]:
            print("Erro: CPF / CNPJ deve conter 11 ou 14 dígitos numéricos.")
            continue   
        else:
            """Formata o número como CPF ou CNPJ."""
            if len(cpf_cnpj) == 11:
                print(f'{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}')  # CPF
            elif len(cpf_cnpj) == 14:
                print(f'{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:]}')  # CNPJ 

        # Escrever os dados no PDF
        cnv.setFont('Roboto-Regular', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(15), y - 76, f'Nome: {nome.title()}')
        cnv.drawString(mil_pol_mil(15), y - 94, f'Nacionalidade: {nacionalidade.title()}')
        cnv.drawString(mil_pol_mil(15), y - 112, f'Empresa: {empresa.title()}')
        cnv.drawString(mil_pol_mil(15), y - 130, f'CPF / CNPJ: {cpf_cnpj}')
        break
    return y - 140

def prestador(y):
    cnv.setLineWidth(1)
    cnv.roundRect(mil_pol_mm(10), y - 72, mil_pol_mm(180), 90, 10, stroke=1, fill=0)
    cnv.setFont('Roboto-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(mil_pol_mil(15), y + 26, 'Prestador de Serviço:')
    nome_prest = 'Antonio Gomes Sales Junior'
    nacionalidade_prest = 'Brasil'
    cpf_prest = '217.884.488-02'
    profissao_prest = 'Desenvolvedor'
    
    cnv.setFont('Roboto-Regular', 12) # Fonte padrão
    cnv.drawString(mil_pol_mil(15), y - 6, f'Nome: {nome_prest}')
    cnv.drawString(mil_pol_mil(15), y - 24, f'Nacionalidade: {nacionalidade_prest}')
    cnv.drawString(mil_pol_mil(15), y - 42, f'CPF / CNPJ: {cpf_prest}')
    cnv.drawString(mil_pol_mil(15), y - 60, f'Profissao: {profissao_prest}')
    return y - 90
    
def clausulas(y):
    os.system('cls')
    while True:
        ### Clausula 1 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol_mil(10), y, 'CLÁUSULA 1 – DO OBJETO')    
        servico = input('Digite o servico a ser prestado: ').strip()
        if not servico:
            print("Erro: Tipo de serviço não pode estar vazia.")
            continue
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 20, f'O presente contrato tem como objeto a prestação de serviços: ({servico})')
        
        ### Clausula 2 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol_mil(10), y - 50, 'CLÁUSULA 2 – DO VALOR E FORMA DE PAGAMENTO')        
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
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 70, f'O valor total do contrato será de R$ {valor_servico_float:.2f}, que será pago da seguinte forma:')
        cnv.drawString(mil_pol_mil(10), y - 85, f'Detalhar a forma de pagamento: {forma_pag.capitalize()}')       

        ### Clausula 3 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol_mil(10), y - 115, 'CLÁUSULA 3 – DO OBJETO')
        prazo_servico = input('Digite a data da entrega do servico a ser prestado: ')
        if not prazo_servico or prazo_servico.isalpha():
            print("Erro: A data do serviço e invalido ou pode estar vazia.")
            continue
        data_inicio = input('Digite o dia de inicio do servico: ')
        data_final = input('Digite o dia de finalizacao do servico: ')      
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 135, f'O prazo para a execução dos serviços será de {prazo_servico} dias, com início em {data_inicio} e término em {data_final},')
        cnv.drawString(mil_pol_mil(10), y - 150, f'podendo ser prorrogado mediante acordo entre as partes.')
        
        ### Clausula 4 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol_mil(10), y - 180, 'CLÁUSULA 4 – DAS OBRIGAÇÕES DO CONTRATADO')
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 200, 'O Contratado se obriga a:')
        cnv.drawString(mil_pol_mil(10), y - 220, '1° - Prestar os serviços descritos na Cláusula 1 com qualidade e eficiência.')
        cnv.drawString(mil_pol_mil(10), y - 235, '2° - Cumprir o prazo de execução estabelecido.')
        cnv.drawString(mil_pol_mil(10), y - 250, '3° - Fornecer relatórios ou resultados periódicos, se necessário.')
        
        ### Clausula 5 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol_mil(10), y - 280, 'CLÁUSULA 5 – DAS OBRIGAÇÕES DO CONTRATANTE')
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 300, 'O Contratante se obriga a:')
        cnv.drawString(mil_pol_mil(10), y - 320, '1°- Efetuar os pagamentos conforme estabelecido na Cláusula 2')
        cnv.drawString(mil_pol_mil(10), y - 335, '2°- Disponibilizar informações e materiais necessários para a execução dos serviços.')
        cnv.drawString(mil_pol_mil(10), y - 350, '3°- Cooperar com o Contratado no que for necessário para a execução do objeto deste contrato.')

        ### Clausula 6 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol_mil(10), y - 380, 'CLÁUSULA 6 – DA RESCISÃO')
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 400, 'Este contrato poderá ser rescindido por qualquer uma das partes, mediante aviso prévio de [X dias],') 
        cnv.drawString(mil_pol_mil(10), y - 420, 'em caso de descumprimento das obrigações aqui estabelecidas. Em caso de rescisão sem justificativa,') 
        cnv.drawString(mil_pol_mil(10), y - 440, 'a parte que rescindir o contrato deverá pagar uma multa de [valor ou percentual] sobre o valor total do' ) 
        cnv.drawString(mil_pol_mil(10), y - 440, 'contrato.')

        ### Clausula 7 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol_mil(10), y - 470, 'CLÁUSULA 7 – DA CONFIDENCIALIDADE')
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 490, 'Ambas as partes se comprometem a manter em sigilo todas as informações confidenciais a que tenham, ')
        cnv.drawString(mil_pol_mil(10), y - 510, 'acesso durante a execução deste contrato, não podendo divulgá-las a terceiros sem prévia autorização.')

        ### Clausula 8 ###
        cnv.drawString(mil_pol_mil(10), y - 540, 'CLÁUSULA 8 – DAS DISPOSIÇÕES GERAIS')
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol_mil(10), y - 560, '1°- A tolerância de qualquer das partes quanto ao descumprimento de qualquer obrigação estabelecida neste contrato não implicará em novação ou renúncia de direito.')
        cnv.drawString(mil_pol_mil(10), y - 580, '2°- Este contrato poderá ser alterado mediante acordo mútuo entre as partes, por escrito.')
        
        return y - 600

# Inicialização de y
y = altura - mil_pol_mil(40)

# Cabeçalho
cabecalho()

# Contratante
y = 745
y = contratante(y)
#if y is not None:
    #divisoria(y)

# Prestador
y = prestador(y - 50)
if y is not None:
    divisoria(y)

# Prestador
y = clausulas(y - 20)
if y is not None:
    divisoria(y)

else:
    print("Erro: 'y' retornado pela função 'prestador' é None.")



cnv.save()