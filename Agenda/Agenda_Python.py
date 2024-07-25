import os
import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho = 'C:\\Users\\anton\\Exercicios_Python\\Banco\\Agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexaoBanco()

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operacao finalizada com sucesso')

def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res

def menuPrincipal():
    os.system('cls')
    print('1 - Inserir novo registro: ')
    print('2 - Deletar registro: ')
    print('3 - Atualizar registro: ')
    print('4 - Consutar registro por ID: ')
    print('5 - Consutar registro por NOME: ')
    print('6 - Sair: ')

def menuInserir():
    os.system('cls')
    vnome = input('Digite o nome: ')
    vtelefone = input('Digite o telefone: ')
    vemail = input('Digite o email: ')
    vsql = "INSERT INTO tb_contatos (T_NOMECONTATOS, T_TELEFONECONTATOS, T_EMAILCONTATOS)VALUES('"+vnome+"', '"+vtelefone+"', '"+vemail+"')"
    query(vcon, vsql)
    os.system('pause')

def menuDeletar():
    os.system('cls')
    vid = input('Digite o ID do registro a ser deletado: ')
    vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATOS ="+vid
    query(vcon, vsql)
    os.system('pause')

def menuAtualizar():
    os.system('cls')
    vid = input('Digite o ID do registro a ser alterado: ')
    r = consultar(vcon, "SELECT * FROM tb_contatos WHERE N_IDCONTATOS ="+vid)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = input('Digite o nome: ')
    vtelefone = input('Digite o telefone: ')
    vemail = input('Digite o email: ')
    if (len(vnome) == 0):
        vnome = rnome
    if (len(vtelefone) == 0):
        vtelefone = rtelefone
    if (len(vemail) == 0):
        vemail = remail
    vsql = "UPDATE tb_contatos SET T_NOMECONTATOS = '"+vnome+"', T_TELEFONECONTATOS = '"+vtelefone+"', T_EMAILCONTATOS = '"+vemail+"' WHERE N_IDCONTATOS ="+vid
    query(vcon, vsql)  
    os.system('pause')

def menuConsutar():
    vsql = 'SELECT * FROM tb_contatos'
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f'ID:{r[0]:_<3} NOME:{r[1]:_<30} TELEFONE:{r[2]:_<14} EMAIL{r[3]:_<30}')
        vcont += 1
        if (vcont >= vlim):
            vcont = 0
            os.system('pause')
            os.system('cls')
    print('Fim da Lista')
    os.system('pause')

def menuConsutarNome():
    vnome = input('Digite o nome: ')
    vsql = "SELECT * FROM tb_contatos WHERE T_NOMECONTATOS LIKE '%"+vnome+"%'"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f'ID:{r[0]:_<3} NOME:{r[1]:_<30} TELEFONE:{r[2]:_<14} EMAIL{r[3]:_<30}')
        vcont += 1
        if (vcont >= vlim):
            vcont = 0
            os.system('pause')
            os.system('cls')
    print('Fim da Lista')
    os.system('pause')

opcao = 0

while opcao != 6:
    menuPrincipal()
    opcao=int(input('Digite uma opcao: '))
    if opcao == 1:
        menuInserir()
    elif opcao == 2:
        menuDeletar()
    elif opcao == 3:
        menuAtualizar()
    elif opcao == 4:
        menuConsutar()
    elif opcao == 5:
        menuConsutarNome()
    elif opcao == 6:
        os.system('cls')
        print('Programa Finalizado')
    else:
        os.system('cls')
        print('Opcao Invalida')
        os.system('pause')

vcon.close
os.system('pause')
    