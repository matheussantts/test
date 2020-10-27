def matriz():

    matriz , linha = [], []

    for i in range(0, 12):
        linha = []
        for j in range(0, 12):
            linha.append(1)
        matriz.append(linha)

    return matriz

matriz = matriz()

soma, soma2 = 0, 0

for i in range(1, 11):
    for j in range(1, i + 1):
        if i > 5:
            break
        soma += matriz[i][j]
        
aux = -1

for m in range(6, 11):
    aux += 1
    for n in range(1, 6 - aux):
        
        print('m', m, 'n', n)
        soma2 += matriz[m][n]

resultado = soma + soma2

print('soma =', resultado)

print(matriz)
