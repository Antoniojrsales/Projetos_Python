#Bibliotecas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os

def mil_pol(mil):
    return mil / 0.35777

# Configuração do PDF
cnv = canvas.Canvas('Contrato.pdf', pagesize=A4)
largura, altura = A4 

# Função de cabeçalho
def cabecalho():
    cnv.setFont('Helvetica-Bold', 16) # Fonte maior e em negrito
    cnv.drawCentredString(largura / 2, altura - mil_pol(20), 'CONTRATO DE PRESTAÇÃO DE SERVIÇOS')
    cnv.setFont('Helvetica', 11) # Fonte padrão
    cnv.drawString(mil_pol(10), altura - mil_pol(35), 'Pelo presente instrumento particular de prestação de serviços')

# Adicionar linhas divisórias
def divisoria(y):
    cnv.setStrokeColor(colors.grey)
    cnv.line(mil_pol(10), y, largura - mil_pol(10), y)

def contratante(y):
    cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(mil_pol(10), y, 'Contratante:')
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
        
        cpf = input('Digite o seu CPF / CNPJ com 11 digitos: ').strip()
        if not cpf.isdigit() or len(cpf) not in [11, 14]:
            print("Erro: CPF / CNPJ deve conter 11 ou 14 dígitos numéricos.")
            continue    

        # Escrever os dados no PDF
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol(10), y - 20, f'Nome: {nome.title()}')
        cnv.drawString(mil_pol(10), y - 40, f'Nacionalidade: {nacionalidade.title()}')
        cnv.drawString(mil_pol(10), y - 60, f'Empresa: {empresa.title()}')
        cnv.drawString(mil_pol(10), y - 80, f'CPF / CNPJ: {cpf}')
        break
    return y - 100

def prestador(y):
    cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
    cnv.drawString(mil_pol(10), y, 'Prestador de Serviço:')
    nome_prest = 'Antonio Gomes Sales Junior'
    nacionalidade_prest = 'Brasil'
    cpf_prest = '217.884.488-02'
    profissao_prest = 'Desenvolvedor'
    
    cnv.setFont('Helvetica', 12) # Fonte padrão
    cnv.drawString(mil_pol(10), y - 20, f'Nome: {nome_prest}')
    cnv.drawString(mil_pol(10), y - 40, f'Nacionalidade: {nacionalidade_prest}')
    cnv.drawString(mil_pol(10), y - 60, f'CPF / CNPJ: {cpf_prest}')
    cnv.drawString(mil_pol(10), y - 80, f'Profissao: {profissao_prest}')

    return y - 100
    
def clausulas(y):
    os.system('cls')
    while True:
        ### Clausula 1 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol(10), y, 'CLÁUSULA 1 – DO OBJETO')    
        servico = input('Digite o servico a ser prestado: ').strip()
        if not servico:
            print("Erro: Tipo de serviço não pode estar vazia.")
            continue
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol(10), y - 20, f'O presente contrato tem como objeto a prestação de serviços: ({servico})')
        
        ### Clausula 2 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol(10), y - 50, 'CLÁUSULA 2 – DO VALOR E FORMA DE PAGAMENTO')        
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
        cnv.drawString(mil_pol(10), y - 70, f'O valor total do contrato será de R$ {valor_servico_float:.2f}, que será pago da seguinte forma:')   

        ### Clausula 3 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol(10), y - 100, 'CLÁUSULA 3 – DO OBJETO')
        cnv.drawString(mil_pol(10), y - 120, f'Detalhar a forma de pagamento: {forma_pag.capitalize()}')    
        prazo_servico = input('Digite a data da entrega do servico a ser prestado: ')
        if not prazo_servico or prazo_servico.isalpha():
            print("Erro: A data do serviço e invalido ou pode estar vazia.")
            continue
        data_inicio = input('Digite o dia de inicio do servico: ')
        data_final = input('Digite o dia de finalizacao do servico: ')      
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol(10), y - 140, f'O prazo para a execução dos serviços será de {prazo_servico} dias, com início em {data_inicio} e término em {data_final},')
        cnv.drawString(mil_pol(10), y - 160, f'podendo ser prorrogado mediante acordo entre as partes.')
        
        ### Clausula 4 ###
        cnv.setFont('Helvetica-Bold', 12) # Fonte maior e em negrito
        cnv.drawString(mil_pol(10), y - 190, 'CLÁUSULA 4 – DAS OBRIGAÇÕES DO CONTRATADO')
        cnv.setFont('Helvetica', 12) # Fonte padrão
        cnv.drawString(mil_pol(10), y - 210, 'O Contratado se obriga a:')
        cnv.drawString(mil_pol(10), y - 230, '1° - Prestar os serviços descritos na Cláusula 1 com qualidade e eficiência.')
        cnv.drawString(mil_pol(10), y - 250, '2° - Cumprir o prazo de execução estabelecido.')
        cnv.drawString(mil_pol(10), y - 270, '3° - Fornecer relatórios ou resultados periódicos, se necessário.')
        
        return y - 290



'''cnv.drawString(mil_pol(10), mil_pol(135), 'CLÁUSULA 5 – DAS OBRIGAÇÕES DO CONTRATANTE')
cnv.drawString(mil_pol(10), mil_pol(130), 'O Contratante se obriga a:')
cnv.drawString(mil_pol(10), mil_pol(125), '1°- Efetuar os pagamentos conforme estabelecido na Cláusula 2')
cnv.drawString(mil_pol(10), mil_pol(120), '2°- Disponibilizar informações e materiais necessários para a execução dos serviços.')
cnv.drawString(mil_pol(10), mil_pol(115), '3°- Cooperar com o Contratado no que for necessário para a execução do objeto deste contrato.')

cnv.drawString(mil_pol(10), mil_pol(110), 'CLÁUSULA 6 – DA RESCISÃO')
cnv.drawString(mil_pol(10), mil_pol(105), 'Este contrato poderá ser rescindido por qualquer uma das partes, mediante aviso prévio de [X dias], em caso de descumprimento das obrigações aqui estabelecidas. Em caso de rescisão sem justificativa, a parte que rescindir o contrato deverá pagar uma multa de [valor ou percentual] sobre o valor total do contrato.')

cnv.drawString(mil_pol(10), mil_pol(100), 'CLÁUSULA 7 – DA CONFIDENCIALIDADE')
cnv.drawString(mil_pol(10), mil_pol(95), 'Ambas as partes se comprometem a manter em sigilo todas as informações confidenciais a que tenham acesso durante a execução deste contrato, não podendo divulgá-las a terceiros sem prévia autorização.')

cnv.drawString(mil_pol(10), mil_pol(90), 'CLÁUSULA 8 – DAS DISPOSIÇÕES GERAIS')
cnv.drawString(mil_pol(10), mil_pol(85), '1°- A tolerância de qualquer das partes quanto ao descumprimento de qualquer obrigação estabelecida neste contrato não implicará em novação ou renúncia de direito.')
cnv.drawString(mil_pol(10), mil_pol(80), '2°- Este contrato poderá ser alterado mediante acordo mútuo entre as partes, por escrito.')'''

# Inicialização de y
y = altura - mil_pol(40)

# Cabeçalho
cabecalho()
divisoria(y)

# Contratante
y = contratante(y - 20)
if y is not None:
    divisoria(y)

# Prestador
y = prestador(y - 20)
if y is not None:
    divisoria(y)

# Prestador
y = clausulas(y - 20)
if y is not None:
    divisoria(y)

else:
    print("Erro: 'y' retornado pela função 'prestador' é None.")



cnv.save()