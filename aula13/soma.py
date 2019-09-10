# Escreva um programa em Python que calcule a soma dos 
# números pares entre 1 e 20 e conta quantos múltiplos de
# sete existem no mesmo intervalo.
s = 0
c = 0 
print('INÍCIO')
for i in range(1, 21):
  print('Processando...')
  print(i)
  if i % 2 == 0:
    print('Atualizando soma em', s, 'com mais', i)
    s = s + i
  if i % 7 == 0:
    print('Encontrei mais um!')
    c = c + 1    
print('Soma dos pares=', s)
print('Contagem dos múltiplos de 7=', c)
print('FIM')
