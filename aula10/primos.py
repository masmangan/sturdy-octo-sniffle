# 2019-09-03
# marco.mangan@pucrs.br
# Escreva um programa em Python que apresenta
# todos os números primos entre
# zero e um valor informado pelo teclado.
print("Informe o valor de x:")
x = int( input() )
for n in range(0, x + 1):
  cont = 0
  for d in range(1, n + 1):
    if n % d == 0:
      cont = cont + 1
  if cont == 2:
    print("PRIMO!", n)
  else:
    print("Não é primo!", n)
