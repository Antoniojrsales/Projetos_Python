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

vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATOS = 3"

def deletar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro deletado')
    except Error as ex:
        print(ex)

deletar(vcon, vsql)