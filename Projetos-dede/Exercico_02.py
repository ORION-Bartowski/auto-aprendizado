saque=int(input('Digite o valor asse sacado'))
nota_200= 0
nota_100= 0
nota_50= 0
nota_20= 0
nota_10= 0
nota_5= 0
nota_2= 0

if saque >= 200:
    nota_200 = saque // 200
    saque = saque % 200
    print(f'são tantas {nota_200} de 200')

if saque >= 100:
    nota_100 = saque // 100
    saque = saque % 100
    print(f'são tantas {nota_100} de 100')

if saque >= 50:
    nota_50 = saque // 50
    saque = saque % 50
    print(f'são tantas {nota_50} de 50')

if saque >= 20:
    nota_20 = saque // 20
    saque = saque % 20
    print(f'são tantas {nota_20} de 20')

if saque >= 10:
    nota_10 = saque // 10
    saque = saque % 10
    print(f'são tantas {nota_10} de 10')

if saque >= 5:
    nota_5 = saque // 5
    saque = saque % 5
    print(f'são tantas {nota_5} de 5')

if saque >= 2:
    nota_2 = saque // 2
    saque = saque % 2
    print(f'são tantas {nota_2} de 2')