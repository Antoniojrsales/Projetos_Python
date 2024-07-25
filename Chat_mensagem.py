import os

mensagens = []

nome = input('Nome: ')

while True:
    os.system('cls') #Limpando O terminal#

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])

    print('____________________')

    texto = input('mensagem: ') #Obtendo o texto#
    if texto == 'fim'.lower():
        break

    mensagens.append({
        'nome': nome,
        'texto': texto
    }) #Adicionando mensagem na lista#