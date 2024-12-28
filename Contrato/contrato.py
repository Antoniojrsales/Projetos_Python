#Bibliotecas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

def mil_pol(mil):
    return mil / 0.35777

# Configuração do PDF
cnv = canvas.Canvas('Contrato.pdf', pagesize=A4)
largura, altura = A4 

# Função de cabeçalho
def cabecalho():
    cnv.setFont('Helvetica-Bold', 16) # Fonte maior e em negrito
    cnv.drawCentredString(largura / 2, altura - mil_pol(20), 'CONTRATO DE PRESTAÇÃO DE SERVIÇOS')
    cnv.setFont('Helvetica', 10) # Fonte padrão
    cnv.drawString(mil_pol(10), altura - mil_pol(35), 'Pelo presente instrumento particular de prestação de serviços, de um lado')

# Adicionar linhas divisórias
def divisoria(y):
    cnv.setStrokeColor(colors.grey)
    cnv.line(mil_pol(10), y, largura - mil_pol(10), y)

def contratante(y):
    cnv.setFont('Helvetica', 12) # Fonte padrão
    cnv.drawString(mil_pol(10), y, 'Contratante:')
    while True:
        nome = input('Digite o seu nome contratante: ').strip()
        if not nome:
            print("Erro: Nome não pode estar vazio.")
            continue
        
        nacionalidade = input('Digite o pais que nasceu: ').strip()
        if not nacionalidade:
            print("Erro: Nacionalidade não pode estar vazia.")
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
        cnv.drawString(mil_pol(10), y - 20, f'Nome: {nome}')
        cnv.drawString(mil_pol(10), y - 40, f'Nacionalidade: {nacionalidade}')
        cnv.drawString(mil_pol(10), y - 60, f'Empresa: {empresa}')
        cnv.drawString(mil_pol(10), y - 80, f'CPF / CNPJ: {cpf}')
        break
    return y - 100

'''def prestador():
    cnv.drawString(mil_pol(10), mil_pol(230), 'Prestador de Serviço:')
    nome_prest = input('Digite o seu nome prestador: ')
    nacionalidade_prest = input('Digite o pais que nasceu: ')
    cpf_prest = input('Digite o seu CPF / CNPJ: ')
    profissao_prest = input('Digite a profissao: ')
    
    cnv.drawString(mil_pol(10), mil_pol(225), f'Nome: {nome_prest}')
    cnv.drawString(mil_pol(10), mil_pol(220), f'Nacionalidade: {nacionalidade_prest}')
    cnv.drawString(mil_pol(10), mil_pol(215), f'CPF / CNPJ: {cpf_prest}')
    cnv.drawString(mil_pol(10), mil_pol(210), f'Profissao: {profissao_prest}')

cnv.drawString(mil_pol(10), mil_pol(200), 'CLÁUSULA 1 – DO OBJETO')
desc_servico = input('Digite o servico a ser prestado: ')
cnv.drawString(mil_pol(10), mil_pol(195), f'O presente contrato tem como objeto a prestação de serviços de {desc_servico}')

cnv.drawString(mil_pol(10), mil_pol(190), 'CLÁUSULA 2 – DO VALOR E FORMA DE PAGAMENTO')
valor_servico = input('Digite o valor do servico a ser prestado: ')
forma_pag = input('Digite a forma de pagamento do servico a ser prestado [Vista, Parcelado, Com vencimentos]: ')
cnv.drawString(mil_pol(10), mil_pol(185), f'O valor total do contrato será de R$ {valor_servico}, que será pago da seguinte forma:')
cnv.drawString(mil_pol(10), mil_pol(175), f'Detalhar a forma de pagamento: {forma_pag}')

cnv.drawString(mil_pol(10), mil_pol(170), 'CLÁUSULA 3 – DO OBJETO')
prazo_servico = input('Digite a data da entrega do servico a ser prestado: ')
data_inicio = input('Digite o dia de inicio do servico')
data_final = input('Digite o dia de finalizacao do servico')
cnv.drawString(mil_pol(10), mil_pol(165), f'O prazo para a execução dos serviços será de {prazo_servico} dias, com início em {data_inicio} e término em {data_final}, podendo ser prorrogado mediante acordo entre as partes.')'''

# Gerar PDF
y = altura - mil_pol(40)
cabecalho()
divisoria(y)
y = contratante(y - 20)
divisoria(y)
#prestador()

cnv.save()