# Listas
# Exercício 1, Lista 3

convidados = ["Ana", "Carlos", "Bruno", "Ana"]
# Adicionar Pedro na lista de convidados
convidados.append("Pedro")
# Remover Bruno
convidados.remove("Bruno")
# Colocar em ordem alfabética
convidados.sort()
# Adicionar Fabiano em primeiro lugar na lista
convidados.insert(0, "Fabiano")
# Remover Pedro da lista
convidados.remove("Pedro")  # Removendo Pedro corretamente
# Contar a quantidade de Anas
quantidade_anitas = convidados.count("Ana")
# Contar quantidade de convidados
quantidade_convidados = len(convidados)

# Imprimir resultados
print(convidados)
print(f"Quantidade de Anas: {quantidade_anitas}")
print(f"Quantidade total de convidados: {quantidade_convidados}")
