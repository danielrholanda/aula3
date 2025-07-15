entrada = input('Você quer [entrar ou sair]' )
entrada = entrada.lower() # arruma o problema caso usuario escreva em maiusculo
if entrada == 'entrar':
    print('Seja Bem Vindo, entrou no sistema')
elif entrada == 'sair':
    print('vocÊ saiu do sistema...')
else:
    print('Voce não digitou nem entrar e nem sair')
