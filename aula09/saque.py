# Saque bancário
# 2019-08-30
# Escreva um programa em Python que recebe um valor real. O valor representa um montante em dinheiro. O programa deve apresentar a menor quantidade possível de numerário que equivale ao valor da entrada. 
# Exemplo:
# Informe valor:
# 127.00
# Resposta:
# 1 x notas de R$ 100,00
# 0 x notas de R$ 50,00
# 1 x notas de R$ 20,00
# 0 x notas de R$ 10,00
# 1 x notas de R$ 5,00
# 1 x notas de R$ 2,00 
# 0 x moedas de R$ 1,00 
# 0 x moedas de R$ 0,50 
# 0 x moedas de R$ 0,25 
# 0 x moedas de R$ 0,10
# 0 x moedas de R$ 0,05
# 0 x moedas de R$ 0,01

print('Informe valor:') # Ler n
#n = float( input() )
n = 4.79

print('Valor informado R$', n)
sobra = n

n100 = sobra // 100
if n100 != 0:
  print(n100, "x", "notas" ,"de R$ 100.")
  sobra = n % 100
  print('Sobra: R$', sobra)

n50 = sobra // 50
if n50 != 0:
  print(n50, "x notas de R$ 50.")
  sobra = sobra % 50
  print('Sobra: R$', sobra)

n20 = sobra // 20
if n20 != 0:
  print(n20, "x notas de R$ 20.")
  sobra = sobra % 20
  print('Sobra: R$', sobra)

n10 = sobra // 10
if n10 != 0: 
  print(n10, "x notas de R$ 10.")
  sobra = sobra % 10
  print('Sobra: R$', sobra)

n5 = sobra // 5
if n5 != 0:
  print(n5, "x notas de R$ 5.")
  sobra = sobra % 5
  print('Sobra: R$', sobra)

n2 = sobra // 2
if n2 != 0:
  print(n2, "x notas de R$ 2.")
  sobra = sobra % 2
  print('Sobra: R$', sobra)

n1 = sobra // 1
if n1 != 0:
  print(n1, "x notas de R$ 1.")
  sobra = sobra % 1
  print('Sobra: R$', sobra)  

n050 = sobra // 0.50
if n050 != 0:
  print(n050, "x moedas de R$ 0,50.")
  sobra = sobra % 0.50
  print('Sobra: R$', sobra)

n025 = sobra // 0.25
if n025 != 0:
  print(n025, "x moedas de R$ 0,25.")
  sobra = sobra % 0.25
  print('Sobra: R$', sobra)

n010 = sobra // 0.10
if n010 != 0:
  print(n010, "x moedas de R$ 0,10.")
  sobra = sobra % 0.10
  print('Sobra: R$', sobra)    

n005 = sobra // 0.05
if n005 != 0:
  print(n005, "x moedas de R$ 0,05.")
  sobra = sobra % 0.05
  print('Sobra: R$', sobra)    

n001 = sobra // 0.01
if n001!= 0:
  print(n001, "x moedas de R$ 0,01.")
  sobra = sobra % 0.01
  print('Sobra: R$', sobra)