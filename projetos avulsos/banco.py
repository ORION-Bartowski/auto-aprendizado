saque = float(input('digite o valor de saque: \n'))

if saque >= 100:
    notasCem = saque // 100
    saque %= 100
    print(f'São {int(notasCem)} notas de Cem Reais R$100')
if saque >= 50:
    notasCinquenta = saque // 50
    saque %= 50
    print(f'São {int(notasCinquenta)} notas de Cinqueta Reais R$50')
if saque >= 20:
    notasVinte = saque // 20
    saque %= 20
    print(f'São {int(notasVinte)} notas de Vinte Reais R$20')
if saque >= 10:
    notasDez = saque // 10
    saque %= 10
    print(f'São {int(notasDez)} notas de Dez reias R$10')
if saque >= 5:
    notasCinco = saque // 5
    saque %= 5
    print(f'São {int(notasCinco)} notas de Cinco R$5')
if saque >= 2:
    notasDois = saque // 2
    saque %= 2
    print(f'São {int(notasDois)} notas de Dois R$2')
if saque >= 1:
    moedaUm = saque // 1
    saque %= 1
    print(f'São {int(moedaUm)} moedas de um R$1')
if saque >= 0.50:
    moedaCinquenta = saque / 0.50
    saque %= 0.50
    print(f'São {int(moedaCinquenta)} moedas de cinqueta centavos R$0.50')
if saque >= 0.25:
    vinticinco = saque / 0.25
    saque %= 0.25
    print(f'São {int(vinticinco)} moedas de vinte cinco centavos R$0.25')
if saque >= 0.10:
    Dez = saque / 0.10
    saque %= 0.10
    print(f'São {int(Dez)} moedas de dez centavos R$0.10')
if saque >= 0.05:
    cincocentavo = saque / 0.05
    saque %= 0.05
    print(f'São {int(cincocentavo)} moedas de cinco Centavos R$0.05')
