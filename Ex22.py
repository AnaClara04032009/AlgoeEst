palavras= []
for i in range(6): 
    palavras=input("Digite uma palavra")
    palavras.append(palavras)
total= 0 
for palavra in palavras:
    if len (palavra) > 5:
         total+= 1
    print("total de palavras com mais de 5 letras é: ", total)