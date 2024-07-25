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

vcon =conexaoBanco()

vsql = """CREATE TABLE tb_contatos (
                N_IDCONTATOS INTEGER PRIMARY KEY AUTOINCREMENT,
                T_NOMECONTATOS TEXT (30),
                T_TELEFONECONTATOS TEXT (14),
                T_EMAILCONTATOS TEXT (30)

);"""

def criarTabela(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print('Tabela Criada')
    except Error as ex:
        print(ex)

criarTabela(vcon, vsql)

vcon.close()