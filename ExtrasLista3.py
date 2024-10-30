#Relembrando
#FOR
for i in range(1, 11):
    print(i)
#AJUDANTE
convidados = ["Ana", "Carlos", "Bruno", "Maria"]
for convidado in convidados:
    print(convidado)  
convidados += convidados 
print(convidados) 
#while
tamanho = 0
while tamanho <= 10:
    print(f"Balão está ficando cheio {tamanho}")
    tamanho += 1
num = 7
numero = int(input("Tente acertar o número (escolha entre 0 e 10): "))

while numero != num:  # Use != em vez de <>
    print("Não foi dessa vez")
    numero = int(input("Tente novamente: "))  # Pergunta novamente até acertar

print("Parabéns, você acertou!")


