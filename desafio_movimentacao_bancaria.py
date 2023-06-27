from datetime import datetime
import os

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 1000
extato = []
deposito = 0
saque = 0
data = ''

# Saldo Inicial

while True:
    print('Saldo atual: {:.2f}'.format(saldo))
    print(menu)
    opcao = input('Digite a sua opção: ')

    # Depositar

    if opcao == '1':
        print('Opção escolhida: Depositar')
        deposito = abs(int(input('Valor a ser depositado: ')))
        saldo += deposito
        data = datetime.today().strftime('%d/%m/%Y %H:%M')

        lancamento = ['D', +deposito, data, saldo]
        extato.append(lancamento)

        print('Deseja continuar?')
        print('[0] para Sair ou Enter para continuar.\n')
        continuar = input('Digite a sua opção: ')
        if continuar == 0:
            break
        os.system("cls")

    # Sacar

    if opcao == '2':
        print('Opção escolhida: Sacar')
        saque = abs(int(input('Valor a ser depositado: ')))
        if saque <= saldo:
            saldo -= saque
            data = datetime.today().strftime('%d/%m/%Y %H:%M')
        else:
            print('Valor digitado invalido!')

        lancamento = ['C', -saque, data, saldo]
        extato.append(lancamento)

        print('Deseja continuar?')
        print('[0] para Sair ou Enter para continuar.\n')
        continuar = input('Digite a sua opção: ')
        if continuar == 0:
            break
        os.system("cls")

    # Extrato

    if opcao == '3':
        print('Opção escolhida: Extrato\n')
        print(' Natureza  | Valor  |  Data  |  Saldo \n')
        for x in zip(extato):
            print(x)

        print('\nSaldo atual: {:.2f}, Data: {}\n'.format(saldo, data))
        print('\nDeseja continuar?')
        print('[0] para Sair ou Enter para continuar.\n')
        continuar = input('Digite a sua opção: ')
        if continuar == 0:
            break
        os.system("cls")

    # Sair

    if opcao == '0':
        print('Até breve!')
        break

print('\nMuito Obrigado por usar nossos serviços!')
