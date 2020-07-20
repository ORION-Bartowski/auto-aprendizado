#ativo = False;

#print(ativo);
"""not = negação."""
#print(not ativo);
"""
negação.
o not inverte a variavel booleano. se for False vira True se for True vira False.
"""
"""ou = or"""

ativo = True
logado = False
print(ativo or logado)

"""
aqui em cima di diz se alguma dessas duas variaveis for true
ele vai responde com true.
ele so responde como false se todas forem false.
"""
"""
- estiver entre aspas simples -> 'uma string',
- estiver entre aspas duplas -> "uma string",
- estiver entre aspas simples tirplas -> '''uma string''',
- estiver entre aspas duplas triplas como nesse comentario é uma string tbm.
"""
nome1 = """
uma string tipo tripla duplas aspas, pode conter qualquer frase com qualquer nome,
pode ser usada como comentaria para o codico, e para ser exibida como estar escrita
do jeitinho do codico fonto original, como esse comentario que estar atribuida a observações.
obrigado pela atenção ate a proxima. 
lower = menusculo
upper = maiusculo
split = "lista" -> trasforma em uma lista de str.
sempre que nos falamos de lista a primeira letra é o zero e o resto pego o rumo;
por exeplo.{
E u g e n i o
0 1 2 3 4 5 6 7
Eugenio do carmo de oliveira
e=0,u=1,g=2,e=3,n=4,i=5,o=6,es=7,d=8,o=9,es=10,c=12,a=12,r=13,m=14,es=15,o=16,l=17,i=18,v=19,i=20,r=21,a=22.23
"""

nome = """Eugenio do carmo de oliveira"""

print(type(nome))
print(nome.lower())
print(nome.upper())
nome = nome.upper()
print(type(nome))
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])
print(nome.split()[2])
print(nome.split()[3])
print(nome.split()[4])
nome = nome.lower()
print(type(nome))
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])
print(nome.split()[2])
print(nome.split()[3])
print(nome.split()[4])

#novo codico
print(nome[::-1])
nome = (nome[::-1])
print(nome[::-1])