print('********************** Python Calculador **********************')
print('')
print('Selecione o número da operação desejada: ')
print('')
print('''1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão''')
print('')
opcao = int(input('Digite a sua opção (1/2/3/4): '))
if((opcao <= 0) or (opcao >= 5)):
    while((opcao <= 0) or (opcao >= 5)):
        print('Opção invalida!')
        opcao = int(input('Digite a sua opção (1/2/3/4): '))
valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
if opcao == 1:
    resp = valor_1 + valor_2
    print(f'{valor_1} + {valor_2} = {resp} ')
elif opcao == 2:
    resp = valor_1 - valor_2
    print(f'{valor_1} - {valor_2} = {resp} ')
elif opcao == 3:
    resp = valor_1 * valor_2
    print(f'{valor_1} * {valor_2} = {resp} ')
else:
    resp = valor_1 / valor_2
    print(f'{valor_1} / {valor_2} = {resp} ')

