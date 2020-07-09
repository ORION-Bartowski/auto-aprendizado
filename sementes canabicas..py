"""
sementes de canabis podem ser modificadas geneticamente aqui nos podemos
verificar quantas sementes você tera no fim do processo.
"""
cont = 0
while cont == False:
    Sementes = int(input("quantas sementes você tem disponivel:\n"))
    especies = ((Sementes-1)/2)*Sementes
    print("você tera:",especies,"diferentes!")
    cont = int(input("digite 0 para prosseguir e qualquer outro numero para sair:\n"))
else:
    nota = int(input("esta satisfeito?\nDe uma nota de 0 a 10:\n"))
    print("você deu a nota",nota,"estamos satisfeito com sua colaboração")
