fluxo_caixa = []

print('-'*12)
print('@ Fluxo de Caixa')
print('-'*12)
print('1- Adicionar Receita')
print('2- Adicionar Despesa')
print('\n# Digite outro numero para encerrar #\n')

def adicionar_transacao():
    nome = input('Nome: ')
    valor = float(input('Valor: '))
    fluxo_caixa.append({
        'nome': nome,
        'valor': valor
    })
    
while True:
    opcao = int(input('Digite a Opcao: '))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

total = 0
for fc in fluxo_caixa:
    print('Nome:', fc['nome'], ', Valor: R$', fc['valor'])
    total += fc['valor']

print('Saldo Atual: R$', total)
    