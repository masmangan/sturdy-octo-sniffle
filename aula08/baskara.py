# https://repl.it/@masmangan/StupendousJovialProlog
# Báskara
from math import sqrt, pow

print('Informe o valor de a: ')
a = float( input() ) # Ler a
print('Informe o valor de b: ')
b = float( input() ) # Ler b
print('Informe o valor de c: ')
c = float( input() ) # Ler c

print(a, 'x^2 +', b, ' x +', c) # Mostra equação ao usuário

# Verificar se a diferente de zero
if a == 0:
  print('O valor de a deve ser diferente de zero.')
  print('==> Execução cancelada!')
else: # a != 0
  delta = pow(b, 2) - 4 * a * c
  # Verificar se delta é negativo
  if delta < 0:
    print('Não existem raízes nos números reais.')
    print('==> Impossível calcular!')
  else: # delta >= 0 and a != 0
    x1 = (-1 * b + sqrt(delta)) / (2 * a)
    x2 = (-1 * b - sqrt(delta)) / (2 * a)
    if delta == 0: # and a != 0
      print('Única raiz: ', x1)
    else: # delta > 0 and a != 0
      print('Primeira raiz: ', x1)
      print('Segunda raiz: ', x2)

print('**Final**')




