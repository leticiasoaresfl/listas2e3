
# Online Python - IDE, Editor, Compiler, Interpreter
media=float
n1 = float (input ("Digite a primeira nota: "))
n2 = float (input ("Digite a segunda nota: "))
n3 = float (input ("Digite a terceira nota: "))

if (n1 > n2): 
   media = (n1*4 + n3*6)/10 
elif (n1 < n2):
    media = (n2*4 + n3*6)/10 
    print (f'A media foi de: {media}')
if media < 3:
    print(f'A média foi de {media} e o aluno está REPROVADO')
elif media >= 3 and media < 5:
    print(f'Precisa reavaliar média de {media}')
else:  # Não precisa de condição
    print(f'A média foi de {media} e você está APROVADO')