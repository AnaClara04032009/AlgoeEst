# isso e um comentario 
# print ("mensagem") #inves de escreval a gente coloca print
# idade= 6
# altura= 0.50
# peso= 5.950
# nome= "francisco"
# print (idade, altura, peso, nome)

# nao e necessario declarar a variavel, mas deve-se declarar um valor quando se utiliza um input, o tipo padao que e string
#entao deve-se declarar o seu tipo caso contrario 

nome= input("insira seu nome")   #string e str = caractere
idade= int(input("insira sua idade"))  #int e inteiro 
peso= float(input("insira seu peso")) #float e real como fazziamos no fluxograma
print(f"{nome} {idade} anos {peso} kg") # se utiliza chaves para chamar uma variavel dentro da string