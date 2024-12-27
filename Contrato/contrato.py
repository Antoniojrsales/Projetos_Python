from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def mil_pol(mil):
    return mil / 0.35777

cnv = canvas.Canvas('Contrato.pdf')

def cabecalho():
    cnv.drawString(mil_pol(60), mil_pol(280), 'CONTRATO DE PRESTAÇÃO DE SERVIÇOS')
    cnv.drawString(mil_pol(10), mil_pol(260), 'Pelo presente instrumento particular de prestação de serviços, de um lado')

def contratante():
    cnv.drawString(mil_pol(10), mil_pol(250), 'Contratante:')
    nome = input('Digite o seu nome contratante: ')
    nacionalidade = input('Digite o pais que nasceu: ')
    cpf = input('Digite o seu CPF / CNPJ: ')
    empresa = input('Digite o nome da Empresa: ')
    
    cnv.drawString(mil_pol(10), mil_pol(245), f'Nome: {nome}')
    cnv.drawString(mil_pol(10), mil_pol(240), f'Nacionalidade: {nacionalidade}')
    cnv.drawString(mil_pol(10), mil_pol(235), f'CPF / CNPJ: {cpf}')
    cnv.drawString(mil_pol(10), mil_pol(230), f'Empresa: {empresa}')

def prestador():
    cnv.drawString(mil_pol(10), mil_pol(210), 'Prestador de Serviço:')
    nome_prest = input('Digite o seu nome prestador: ')
    nacionalidade_prest = input('Digite o pais que nasceu: ')
    cpf_prest = input('Digite o seu CPF / CNPJ: ')
    profissao_prest = input('Digite a profissao: ')
    
    cnv.drawString(mil_pol(10), mil_pol(205), f'Nome: {nome_prest}')
    cnv.drawString(mil_pol(10), mil_pol(200), f'Nacionalidade: {nacionalidade_prest}')
    cnv.drawString(mil_pol(10), mil_pol(195), f'CPF / CNPJ: {cpf_prest}')
    cnv.drawString(mil_pol(10), mil_pol(190), f'Empresa: {profissao_prest}')

cabecalho()
contratante()
prestador()

cnv.save()