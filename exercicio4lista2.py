# Feito junto com a aula de monitoria, não havia conseguido fazer sozinha
largura = int(input('Digite a largura do retângulo: '))

comprimento = largura * 3

print()

a = 1

while a <= largura:

    if a == 1 or a == largura:
        print(f'{"#"*comprimento}')
    else:
     
        vazio = comprimento - 2  
        print(f'#{" "*vazio}#')
    a += 1