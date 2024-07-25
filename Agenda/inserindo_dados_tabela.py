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

nome = input('Digite o nome: ')
telefone = input('Digite o telefone: ')
email = input('Digite o email: ')

vsql = "INSERT INTO tb_contatos(T_NOMECONTATOS, T_TELEFONECONTATOS, T_EMAILCONTATOS)VALUES('"+nome+"', '"+telefone+"', '"+email+"')"

def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)

inserir(vcon, vsql)