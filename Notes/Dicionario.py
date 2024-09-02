pessoa = {"nome": "Gabriel", "idade": 21}

pessoa = dict(nome = "Gabriel", idade = 21)

#Adicionando
pessoa["telefone"] = "1111-1111"

#Acessando os valores
print(pessoa["nome"])

#Sobrescrevendo 
pessoa["idade"] = 22
print(pessoa["idade"])

#Estrutura aninhada
contatos = {
    "email-1@gmail.com": {"nome":"nome1", "telefone":"telefone1"},
    "email-2@gmail.com": {"nome":"nome2", "telefone":"telefone2"},
    "email-3@gmail.com": {"nome":"nome3", "telefone":"telefone3"}
}
#Acesso
contatos["email-1@gmail.com"]["telefone"]

#iterando
for chave, valor in contatos.items():
    print(chave, valor)

#METODOS
contatos2 = {
    "email-1@gmail.com": {"nome":"nome1", "telefone":"telefone1"},
    "email-2@gmail.com": {"nome":"nome2", "telefone":"telefone2"},
    "email-3@gmail.com": {"nome":"nome3", "telefone":"telefone3"}
}

#.clear
contatos2.clear()

#.copy
contatos2.copy()

#.fromkeys
teste = dict.fromkeys(["nome", "telefone"])
print(teste)

teste_2 = dict.fromkeys(["nome", "telefone"], "vazio")
print(teste_2)

#.get
contatos3 = {
    "email-5@gmail.com": {"nome":"nome5", "telefone":"telefone5"}
}

print(contatos3.get("email-5@gmail.com", {}))
print(contatos3.get("chave", {}))

#.items
contatos4 = {
    "email-5@gmail.com": {"nome":"nome5", "telefone":"telefone5"}
}
print(contatos4.items())

#.keys
contatos5 = {
    "email-5@gmail.com": {"nome":"nome5", "telefone":"telefone5"}
}
print(contatos5.keys())

#.setdefault
contato6 = {"nome": "Gabriel", "telefone": "1234-5678"}
print(contato6.setdefault("nome", "Giovana"))
print(contato6)
print(contato6.setdefault("idade", 21))
print(contato6)