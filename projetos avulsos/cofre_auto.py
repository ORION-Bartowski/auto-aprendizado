#variaveis
porta = int(input(print("digite o valor da porta desejada: ")))
coluna = 0
linha = 0
quantidade_de_portas = 5
porta1 = porta
#contador
if porta1 > quantidade_de_portas:
    linha = porta1 // quantidade_de_portas
    porta1 = porta1 % quantidade_de_portas
if porta1 < quantidade_de_portas and porta1 >= 1:
    linha = linha + 1
    coluna = porta1
    porta1 = 0
if coluna == 0:
    coluna = coluna + quantidade_de_portas
#aqui conferimos como estão indo a variavel.
print(f'linha:{linha}\ncoluna:{coluna}\nporta:{porta}')
