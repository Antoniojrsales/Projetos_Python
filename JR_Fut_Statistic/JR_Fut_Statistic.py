#Bibliotecas
import os
import sqlite3
from sqlite3 import Error

#Funcao que cria a conexao com o BD sqllite3
def ConexaoBanco():
    caminho = 'simulador_apostas.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
        print('Conexao estabelecida com sucesso.')
    except Error as ex:
        print(f'Erro na conexao. {ex}')
    return con

vcon = ConexaoBanco()

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Operacao realizada com sucesso')
    except Error as ex:
        print(f'Erro ao executara query {ex}')
    
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res

# Função para verificar se a tabela existe
def verificaTabela(conexao, tabela):
    try:
        c = conexao.cursor()
        c.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = c.fetchall()
        print(f"Tabelas encontradas no banco de dados: {tabelas}")
        c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tabela}';")
        res = c.fetchone()
        if res:
            print(f"Tabela {tabela} encontrada.")
        else:
            print(f"Tabela {tabela} não encontrada.")
        return res
    except Error as ex:
        print(f"Erro ao verificar tabela: {ex}")
        return None


def menuPrincipal():
    os.system('cls')
    print('1 - Inserir novo registro')
    print('2 - Deletar registro')
    print('3 - Atualizar registro')
    print('4 - Consultar registro pelo ID')
    print('5 - Consultar registro pelo Campeonato')
    print('6 - Sair')

def menuInserir():
    os.system('cls')
    #Criando as variaveis para entradas no BD
    data = input('Digite a data do evento: ')
    competicao = input('Digite a competicao do evento: ')
    time_casa = input('Digite o time Casa do evento: ')
    result_casa = input('Digite o resultado casa do evento: ')
    time_visit = input('Digite o time Visitante do evento: ')
    result_visit = input('Digite o resultado visitante do evento: ')
    estrategia_mercado = input('Digite a estrategia/mercado do evento: ')
    aposta_valor = input('Digite a aposta/valor do evento: ')
    lucro_prejuizo = input('Digite o lucro/prejuizo do evento: ')
    odd = input('Digite a ODD do evento: ')
    resultado = input('Digite o resultado [G/R] do evento: ').upper()
    roi = input('Digite a ROI do evento: ')
    vsql = f"""
    INSERT INTO tb_futebol (
        T_DATA, T_COMPETICAO, T_TIMECASA, N_RESULTADOCASA,
        T_TIMEVISITANTE, N_RESULTADOVISITANTE, T_ESTRATEGIA_MERCADO,
        N_APOSTA_VALOR, N_LUCRO_PREJUIZO, N_ODD, T_RESULTADO, N_ROI
    ) VALUES (
        '{data}', '{competicao}', '{time_casa}', '{result_casa}', 
        '{time_visit}', '{result_visit}', '{estrategia_mercado}', 
        '{aposta_valor}', '{lucro_prejuizo}', '{odd}', '{resultado}', '{roi}'
    )
    """
    query(vcon, vsql)

def menuDeletar():
    print()

def menuAtualizar():
    print()

def menuconsultarId():
    print()

def menuconsultarCampeonato():
    print()

# Verifica se a tabela existe antes de iniciar o programa
if not verificaTabela(vcon, 'tb_futebol'):
    print("Certifique-se de que a tabela 'tb_futebol' existe no banco de dados.")
else:
    opcao = 0

    while True:
        menuPrincipal()
        opcao = int(input('Digite a opcao desejada: '))
        if opcao == 1:
            menuInserir()
        elif opcao == 2:
            menuDeletar()
        elif opcao == 3:
            menuAtualizar()
        elif opcao == 4:
            menuconsultarId()
        elif opcao == 5:
            menuconsultarCampeonato()
        elif opcao == 6:
            os.system('cls')
            print('Programa finalizado')
            break
        else:
            os.system('cls')
            print('Opcao invalida digite uma opcao valida: ')
            os.system('pause')

vcon.close


