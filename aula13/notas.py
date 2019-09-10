# Escreva um programa em Python que calcule a média da
# de uma turma, a nota mínima e a máxima e quantos alunos
# tem nota abaixo de 4.0. O programa recebe uma lista
# as notas dos alunos.
# Exemplo:
# 10,0 7,0 8,2 5,1 10,0 4,0 1,5

media = 0
minima = 10.0
maxima = 0.0
rep = 0
soma = 0
quant = 0
for nota in [10.0, 7.0, 8.2, 5.1, 10.0, 4.0, 1.5]:
	print(nota)
	quant = quant + 1
	soma = soma + nota
	if minima > nota:
		minima = nota
	if maxima < nota:
		maxima = nota
	if nota < 4.0:
		rep = rep + 1
media = soma / quant
print('Quant=', quant)
print('Soma=', soma)
print('Media=', media)
print('Min=', minima)
print('Max=', maxima)
print('Rep=', rep)

