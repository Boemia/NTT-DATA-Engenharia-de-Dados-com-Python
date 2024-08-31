#lista 
frutas = []

frutas = ["laranja", "morango"]

#Faz das letras os itens da lista
letras = list("letras")

#Gera a lista com o "range"
numeros = list(range(10))

carro = ["Corsa", "2006", "São Paulo"]

print(frutas, letras, carro)

#Selecionando
cores = ["Azul", "Verde", "Amarelo"]
print(cores[1], cores[-1])

#Matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0][2])

#Selecionando
lista = list("python")

print(lista[2:], lista[1:5], lista[::], lista[::-1])

#Iterar
peças = ["placa-mão", "processador", "placa-de-video"]
for peça in enumerate(peças):
    print(peça)

#Append
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros2:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)