# Escreva um programa em Python que recebe valores inteiros informados via teclado. A digitação termina quando o usuário digitar
#99. Ao final da digitação, apresente a soma dos números digitados
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