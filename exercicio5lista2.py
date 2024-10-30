# BOLETO
print ("INSERÇÃO DADOS DO RECIBO:")
produto = input("Digite o nome do produto: ")
if not produto.isalpha():
    print("ERRO: produto incorreto, escreva o nome do produto somente com letras e sem espaços vazios.")
else:
    numeroserie = input("Digite os 4 números de série:")
    if len(numeroserie) != 4 or not numeroserie.isdigit():
        print("ERRO: número de série não encontrado, apenas 4 números e sem espaços ou caracteres.")
    else:
        valor = float(input("Digite o valor do produto:"))
    print ("----RECIBO----")
    print (f'Produto: {produto}')
    print (f'Série: {numeroserie}')
    print (f'Valor: R${valor}')



    


