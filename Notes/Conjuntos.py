#Criando sets
#set não possui objetos repetidos
print(set([1, 2, 3, 2, 3, 4]))
print(set("abacaxi"))

linguagens = {"python", "java", "python"}
print(linguagens)

#Acessando valores
numeros = {1, 2, 3, 2}
#print(numeros[0]) - É necessário transformar em lista primeiro.
numeros = list(numeros)
print(numeros[0])

carros = {"celta", "uno", "palio"}
for carro in carros:
    print(carro)

#.union
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.union(conjunto_b))
#.intersection
print(conjunto_a.intersection(conjunto_b))
#.difference
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
#.symmetric_difference
print(conjunto_a.symmetric_difference(conjunto_b))

#.issubset
conjunto_c = {1, 2, 3}
conjunto_d = {4, 1, 2, 5, 6, 3}
print(conjunto_c.issubset(conjunto_d))
print(conjunto_d.issubset(conjunto_c))
#.issuperset
print(conjunto_c.issuperset(conjunto_d))
print(conjunto_d.issuperset(conjunto_c))

#.isdisjoint
ex_a = {1, 2}
ex_b = {2, 3}
ex_c = {3, 4}
print(ex_a.isdisjoint(ex_b))
print(ex_a.isdisjoint(ex_c))

#.add
sorteio = {1, 2, 3}
sorteio.add(4)
sorteio.add(3)
print(sorteio)

#.discart
li = {1, 2, 3, 4, 5}
li.discard(2)
print(li)

#.pop
li_2 = {1, 2, 3, 4, 5}
li_2.pop()
li_2.pop()
print(li_2)

#.remove
# = .discart, mas não remove valores que não existem na lista(da erro)

#len
li_3 = {1, 2, 3, 4, 5}
print(len(li_3))

#in
print(3 in li_3)