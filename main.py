opcao = 7

print(f'{" FINANCIAL CONTROL ":=^40}')

while opcao != 0:
    print ('''
           [1] Registrar salário
           [2] Registrar despesa
           [3] Listar Movimentações
           [4] Consultar saldo
           [5] Relatório financeiro
           [0] Sair''')
    opcao = int(input('\nO que deseja fazer? '))

    