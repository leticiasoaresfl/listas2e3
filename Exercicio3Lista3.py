# Inicializando o conjunto de presentes
presentes = {"Ana", "Carlos", "Pedro", "Lucas"}

# Imprimindo os nomes e verificando que Ana não aparece mais de uma vez
print("Presentes:", presentes)

# Verificando se Carlos está na lista
if "Carlos" in presentes:
    print("Carlos está na lista")
else:
    print("Carlos não está na lista")

# Verificando se Beatriz está na lista
if "Beatriz" in presentes:
    print("Beatriz está na lista")
else:
    print("Beatriz não está na lista")

# Adicionando amigo inusitado
presentes.add("Amigo inusitado")
print("Após adicionar amigo inusitado:", presentes)

# Removendo Lucas
presentes.remove("Lucas")
print("Após remover Lucas:", presentes)
