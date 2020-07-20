qtd= int(input('quantas vezes esse loop deve rodar: '))
soma = 0
for c in range(1, qtd +1):
    num = int(input(f'informe o {c}/{qtd} valor: '))
    print(num)
    soma += num
    print(f'a soma é {soma}')
    print(qtd)
    print(c)