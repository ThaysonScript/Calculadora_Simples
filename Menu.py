from funcoes import Operador
from Cabeca import Cabecalho

Cabecalho()
Mn = 'Menu'
print(f'{Mn:>17}')
Cabecalho()

while True:
	opr = str(input('Digite o Operador: '))
	Operador(opr)
	saida = str(input('Deseja execultar mais alguma operação? [S/N] '))
	if saida in 'Ss':
		continue
	elif saida in 'Nn':
		break
	else:
		print('Digite Corretamente!')
print('Finalizando...')
