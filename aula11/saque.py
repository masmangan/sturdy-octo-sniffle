n = 4.70

print('Valor informado R$', n)
sobra = n

for nota in [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]:
  v = sobra // nota
  if v != 0:
    print(v, "x", "de R$", nota)
    sobra = sobra % nota
    print('Sobra: R$', sobra)
