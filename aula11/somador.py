# Escreva um programa em Python que recebe valores inteiros informados via teclado. A digita��o termina quando o usu�rio digitar
#99. Ao final da digita��o, apresente a soma dos n�meros digitados
# Exemplo
# 10
# 10
# 99
# Soma=20

s = 0
while True :
	n = int( input() )
	if n == 99:
		break
	s = s + n

print(s)