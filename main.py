opcao = 7
entradas = []
despesas = []

print(f'{" FINANCIAL CONTROL ":=^40}')

while opcao != 0:
    print('''
           [1] Registrar entrada
           [2] Registrar despesa
           [3] Listar movimentações
           [4] Consultar saldo
           [5] Relatório financeiro
           [0] Sair''')

    opcao = int(input('\nO que deseja fazer? '))

    if opcao == 1:
        continuar = 's'

        while continuar == 's':
            nome = input('Digite o nome da entrada: ')
            valor = float(input('Digite o valor da entrada: '))
            entradas.append((nome, valor))

            print('\nEntrada registrada com sucesso!')
            continuar = input('\nDeseja registrar outra entrada? [s/n] ')

    elif opcao == 2:
        nome = input('Digite o nome da despesa: ')
        valor = float(input('Digite o valor da despesa: '))
        despesas.append((nome, valor))

        print('\nDespesa registrada com sucesso!')

    elif opcao == 3:
        print(f'{" MOVIMENTAÇÕES ":=^40}')
        print('''
        [1] Listar entradas
        [2] Listar despesas
        [3] Voltar ao menu principal''')

        escolha = int(input('\nO que deseja visualizar? '))

        if escolha == 1:
            print(f'\n{" ENTRADAS ":=^40}')

            if len(entradas) == 0:
                print('\nNenhuma entrada registrada.')
            else:
                print(f'{" DESCRIÇÃO ":<25}{" VALOR ":>15}')
                print('-' * 40)

                for movimentacao in entradas:
                    print(
                        f'{movimentacao[0]:<25}'
                        f'R$ {movimentacao[1]:>10.2f}'
                    )

        elif escolha == 2:
            print(f'\n{" DESPESAS ":=^40}')

            if len(despesas) == 0:
                print('\nNenhuma despesa registrada.')
            else:
                print(f'{" DESCRIÇÃO ":<25}{" VALOR ":>15}')
                print('-' * 40)

                for movimentacao in despesas:
                    print(
                        f'{movimentacao[0]:<25}'
                        f'R$ {movimentacao[1]:>10.2f}'
                    )

    elif opcao == 4:
        print('Consulta de saldo ainda será implementada.')

    elif opcao == 5:
        print('Relatório financeiro ainda será implementado.')

    elif opcao == 0:
        print('\nSaindo do Financial Control...')

    else:
        print('\nOpção inválida! Tente novamente.')