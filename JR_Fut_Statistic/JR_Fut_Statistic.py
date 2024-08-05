#Bibliotecas
import os
import sqlite3
from sqlite3 import Error

#Funcao que cria a conexao com o BD sqllite3
def ConexaoBanco():
    file = 'simulador_apostas.db'
    con = None
    try:
        con = sqlite3.connect(file)
        print('Conexao estabelecida com sucesso.')
    except Error as ex:
        print(f'Erro na conexao {ex}')
    return con

vcon = ConexaoBanco()

#Funcao que executa uma operação SQL em um banco de dados usando uma conexão
def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Operacao realizada com sucesso')
    except Error as ex:
        print(f'Erro ao executara query {ex}')
    
#Funcao que executar uma consulta SQL que retorna dados do banco de dados e devolver esses dados ao chamador.
def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res

# Função com tratamento de erro para verificar se a tabela existe ou nao
def verificaTabela(conexao, tabela):
    try:
        c = conexao.cursor()
        c.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
        table = c.fetchall()
        print(f"Tabelas encontradas no banco de dados: {table}")
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
    
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menuPrincipal():
    clear_screen()
    print('1 - Inserir novo registro')
    print('2 - Deletar registro')
    print('3 - Atualizar registro')
    print('4 - Consultar registro pelo ID')
    print('5 - Consultar registro pelo Campeonato')
    print('6 - Sair')

def menuInserir():
    while True:
        clear_screen()
        
        data = input('Digite a data do evento: ').strip()
        if not data:
            print('Data inválida, favor digitar uma data válida.')
            continue
        
        competicao = input('Digite a competição do evento: ').strip()
        if not competicao:
            print('Competição inválida, favor digitar uma competição válida.')
            continue
        
        time_casa = input('Digite o time Casa do evento: ').strip()
        if not time_casa:
            print('Time Casa inválido, favor digitar um time válido.')
            continue
        
        result_casa = input('Digite o resultado casa do evento: ').strip()
        if not result_casa:
            print('Resultado Casa inválido, favor digitar um resultado válido.')
            continue
        
        time_visit = input('Digite o time Visitante do evento: ').strip()
        if not time_visit:
            print('Time Visitante inválido, favor digitar um time válido.')
            continue
        
        result_visit = input('Digite o resultado visitante do evento: ').strip()
        if not result_visit:
            print('Resultado Visitante inválido, favor digitar um resultado válido.')
            continue
        
        estrategia_mercado = input('Digite a estratégia/mercado do evento: ').strip()
        if not estrategia_mercado:
            print('Estratégia/Mercado inválido, favor digitar uma estratégia válida.')
            continue
        
        try:
            aposta_valor = float(input('Digite a aposta/valor do evento: '))
            if not aposta_valor:
                print('Aposta/Valor inválido, favor digitar um valor válido.')
                continue
        except ValueError:
            print('Aposta/Valor inválido, favor digitar um valor válido.')
            continue
        
        try:
            lucro_prejuizo = float(input('Digite o lucro/prejuízo do evento: '))
            if not lucro_prejuizo:
                print('Lucro/Prejuízo inválido, favor digitar um valor válido.')
                continue
        except ValueError:
                print('Lucro/Prejuízo inválido, favor digitar um valor válido.')
                continue

        try:
            odd = float(input('Digite a ODD do evento: '))
            if not odd:
                print('ODD inválida, favor digitar uma ODD válida.')
                continue  
        except ValueError:
                print('ODD inválida, favor digitar uma ODD válida.')
                continue

        resultado = input('Digite o resultado [G/R] do evento: ').strip().upper()
        if not resultado or resultado not in ['G', 'R']:
            print('Resultado inválido, favor digitar "G" ou "R".')
            continue
        
        roi = int(input('Digite a ROI do evento: '))
        if not roi:
            print('ROI inválida, favor digitar um valor válido.')
            continue
    
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
        
        try:
            query(vcon, vsql)
            print('Registro inserido com sucesso.')
        except Exception as e:
            print(f'Erro ao inserir registro: {e}')
        
        continuar = input('Deseja inserir outro registro? (s/n): ').strip().lower()
        if continuar != 's':
            break

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


