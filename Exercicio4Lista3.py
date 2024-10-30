convidados_vip = {
    "Ana": "Salada de frutas",
    "Carlos": "Cerveja",
    "Bruno": "Churrasco",
    "Você": {"Copos": 10, "Arroz": "1kg"}
}

# Verificando o que Carlos irá levar
print(convidados_vip["Carlos"])

# Alterando a comida de Ana
convidados_vip["Ana"] = "Torta Holandesa"
print(convidados_vip["Ana"])

# Adicionando Maria
convidados_vip["Maria"] = "Refrigerante"
print(convidados_vip)

# Verificando os Copos
print(convidados_vip["Você"]["Copos"])

# Adicionando Fabiano
convidados_vip["Fabiano"] = "1kg de maionese e 6 cadeiras"
print(convidados_vip)
