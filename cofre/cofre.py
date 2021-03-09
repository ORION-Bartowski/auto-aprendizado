conta = str(input('digite o numero da conta'))
saque = int(input('digite o valor a ser sacado'))

if saque >= 200:
    notas200 = saque // 200
    saque = saque % 200
    print(f'notas de 200 {notas200}')

if saque >= 100:
    notas100 = saque // 100
    saque = saque % 100
    print(f'notas de 100 {notas100}')

if saque >= 50:
    notas50 = saque // 50
    saque = saque % 50
    print(f'notas de 50 {notas50}')

if saque >= 20:
    notas20 = saque // 20
    saque = saque % 20
    print(f'notas de 20 {notas20}')

if saque >= 10:
    notas10 = saque // 10
    saque = saque % 10
    print(f'notas de 10 {notas10}')

if saque >= 5:
    notas5 = saque // 5
    saque = saque % 5
    print(f'notas de 5 {notas5}')

if saque >= 2:
    notas2 = saque // 2
    saque = saque % 2
    print(f'notas de 2 {notas2}')

