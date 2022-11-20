def Operador(msg):
	if msg not in '+-*/':
		print('Caracter errado!')
	if msg == '+':
		n1 = int(input('Digite o primeiro valor: '))
		n2 = int(input('Digite o segundo valor: '))
		soma = n1 + n2
		print(f'A soma entre os numeros e: {soma}')
	elif msg == '-':
		n1 = int(input('Digite o primeiro valor: '))
		n2 = int(input('Digite o segundo valor: '))
		subt = n1 - n2
		print(f'A subtração entre os numeros e: {subt}')
		
	elif msg == '*':
		n1 = int(input('Digite o primeiro valor: '))
		n2 = int(input('Digite o segundo valor: '))
		mult = n1 * n2
		print(f'A multiplicação entre os numeros e: {mult}')
		
	elif msg == '/':
		n1 = int(input('Digite o primeiro valor: '))
		n2 = int(input('Digite o segundo valor: '))
		div = n1 / n2
		print(f'A divisão entre os numeros e: {div}')
