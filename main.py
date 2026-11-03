opcao = 7
entradas = []
despesas = []

total_entradas = 0
total_despesas = 0

saldo_inicial = float(input('Digite seu saldo inicial: R$ '))

while opcao != 0:
    print(f'\n{" CONTROLE FINANCEIRO ":=^40}')
    print('[1] Registrar entrada')
    print('[2] Registrar despesa')
    print('[3] Listar movimentações')
    print('[4] Consultar saldo')
    print('[5] Relatório financeiro')
    print('[0] Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        continuar = 'S'

        while continuar == 'S':
            nome = input('Descrição da entrada: ')
            valor = float(input('Valor da entrada: R$ '))

            entradas.append((nome, valor))
            total_entradas += valor

            continuar = input('Deseja registrar outra entrada? [S/N] ').upper()

    elif opcao == 2:
        continuar = 'S'

        while continuar == 'S':
            nome = input('Descrição da despesa: ')
            valor = float(input('Valor da despesa: R$ '))

            despesas.append((nome, valor))
            total_despesas += valor

            continuar = input('Deseja registrar outra despesa? [S/N] ').upper()

    elif opcao == 3:
        escolha = 0

        while escolha != 3:
            print(f'\n{" MOVIMENTAÇÕES ":=^40}')
            print('[1] Listar entradas')
            print('[2] Listar despesas')
            print('[3] Voltar ao menu principal')

            escolha = int(input('Escolha uma opção: '))

            if escolha == 1:
                print(f'\n{" LISTAGEM DE ENTRADAS ":=^40}')

                for movimentacao in entradas:
                    print(f'{movimentacao[0]:<25}R$ {movimentacao[1]:>10.2f}')

                print('=' * 40)
                print(f'{" Total de entradas: ":<25}R$ {total_entradas:>10.2f}')

                continuar = input('Deseja visualizar outra movimentação? [S/N] ').upper()

                if continuar == 'N':
                    escolha = 3

            elif escolha == 2:
                print(f'\n{" LISTAGEM DE DESPESAS ":=^40}')

                for movimentacao in despesas:
                    print(f'{movimentacao[0]:<25}R$ {movimentacao[1]:>10.2f}')

                print('=' * 40)
                print(f'{" Total de despesas: ":<25}R$ {total_despesas:>10.2f}')

                continuar = input('Deseja visualizar outra movimentação? [S/N] ').upper()

                if continuar == 'N':
                    escolha = 3

            elif escolha == 3:
                print('Voltando ao menu principal...')

    elif opcao == 4:
        saldo_atual = saldo_inicial + total_entradas - total_despesas

        print(f'\n{" CONSULTA DE SALDO ":=^40}')
        print(f'{" Saldo inicial: ":<25}R$ {saldo_inicial:>10.2f}')
        print(f'{" Saldo atual: ":<25}R$ {saldo_atual:>10.2f}')

    elif opcao == 5:
        saldo_atual = saldo_inicial + total_entradas - total_despesas

        print(f'\n{" RELATÓRIO FINANCEIRO ":=^40}')
        print(f'{" Saldo inicial: ":<25}R$ {saldo_inicial:>10.2f}')
        print(f'{" Entradas registradas: ":<25}{len(entradas):>10}')
        print(f'{" Total de entradas: ":<25}R$ {total_entradas:>10.2f}')
        print(f'{" Despesas registradas: ":<25}{len(despesas):>10}')
        print(f'{" Total de despesas: ":<25}R$ {total_despesas:>10.2f}')
        print('=' * 40)
        print(f'{" Saldo atual: ":<25}R$ {saldo_atual:>10.2f}')

    elif opcao == 0:
        print('Encerrando o sistema...')

    else:
        print('Opção inválida.')