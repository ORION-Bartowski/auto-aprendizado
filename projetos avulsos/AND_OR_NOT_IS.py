"""
AND =   E
OR  =   OU
NOT =   NÃO
IS  =   É

OPERADORES UNARIOS:
NOT
OPERADORES BINARIOS:
AND-OR-IS
"""
ativo = True
logado = True
#se os dois estiver True ele execulta o comando.
if ativo and logado:
    print('Bem vindo usuario!')
else:
    print('voce precisa cadastrar sua conta.')

#para o or um ou outro valor tem que ser True.
if ativo or logado:
    print('Bem vindo usuario!')
else:
    print('voce precisa cadastrar sua conta.')

# se estiver em False execulte isso. um operador de negação trabalha ao contrario.
if not ativo:
    print('voce precisa verificar sua conta, por favor check seu email')
else:
    print('bem vindo usuario')

#
if not ativo:
    print('voce precisa verificar sua conta, por favor check seu email')
else:
    print('bem vindo usuario')

#o valor é comparado com o segundo.
if ativo is True:
    print('bem vindo usuario')
else:
    print('voce precisa verificar sua conta, por favor check seu email')
