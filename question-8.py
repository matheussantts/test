def matriz():

    matriz , linha = [], []

    for i in range(0, 12):
        linha = []
        for j in range(0, 12):
            linha.append(1)
        matriz.append(linha)

    return matriz

matriz = matriz()

soma = 0

for i in range(1, 12):
    for j in range(12 - i, 12):
        print('i', i, 'j', j) 
        soma += matriz[i][j] 
        
print('soma =', soma)

print(matriz)
