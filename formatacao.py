# imc - índice massa corporal
# imc = peso / altura **2
# imc = peso / altura * altura
nome = 'Daniel'
altura = 1.73
peso = 75

imc = peso / (altura * altura)
print(nome,'tem',altura, 'de altura','pesa',peso, 'e seu IMC é',imc)
#f-strings
print(f'{nome} tem {altura} de altura pesa {peso} e seu imc é = {imc:.2f}')