# isso e um comentario 
# print ("mensagem") #inves de escreval a gente coloca print
# idade= 6
# altura= 0.50
# peso= 5.950
# nome= "francisco"
# print (idade, altura, peso, nome)

# nao e necessario declarar a variavel, mas deve-se declarar um valor quando se utiliza um input, o tipo padao que e string
#entao deve-se declarar o seu tipo caso contrario 

# nome= input("insira seu nome")   #string e str = caractere
# idade= int(input("insira sua idade"))  #int e inteiro 
# peso= float(input("insira seu peso")) #float e real como fazziamos no fluxograma
# print(f"{nome} {idade} anos {peso} kg") # se utiliza chaves para chamar uma variavel dentro da string

# pedaco_pizza=5.0
# cliente="john"
# print(type(pedaco_pizza))
# print(type(cliente))


# pedaco_pizza = input ("informe quantos pedaços comeu")
# print(type(pedaco_pizza))


# a=4
# A= "Sally"
# print(a)
# print(A)

# fruta1,fruta2,fruta3= "laranja", "banana", "maça"
# print (fruta1,fruta2,fruta3)

# primeiro_numero=5
# segundo_numero=10
# print (primeiro_numero + segundo_numero)


# nome=input ("qual o vingador mais forte?")
# print(f"ola, {nome}!")
# if nome == "hulk":      #== comparacao      = igual
#      print ("bem vindo vingador mais forte")
# else:
#       print ("acesso negado")


# x= 5
# if x > 2 and x < 10: #ambas as condições devem ser verdadeiras 
#     print ("o numero esta entre 2 e 10 ")
# else:
#     print ("nao esta entre 2 e 10")

# x=5
# if x < 2 or x > 4: # apenas uma condição precisa ser verdadeira 
#     print("o numero é menor que 2 ou maior que 4.")


# x=5
# if not x > 10: #inverte a condicao (x nao e maior que 10)
#     print ("o numero nao e maior que 10 ")

# x= 5
# y=8
# if x > 2 and ( y > 10 or not x == 5):          # a ordem na qual python avalia os operadores logicos e:
#     print ("condicao complexa atendida.")      # 1- not 
# else:                                           # 2- and
#     print ("condição nao atendida")            # 3- or 