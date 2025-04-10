idade = int(input("digite sua idade: "))
sexo = input("digite seu sexo, se e masculino ou feminino")
categoria = input("digite sua categoria")

if idade >= 15:
    print ("artigos infantis")

elif idade >= 15 and idade <= 21 and sexo.lower() == "feminino":
    print("maquiagem e moda")
elif idade >= 15 and idade <= 32 and sexo.lower() == "masculino":
    print(" artigos esportivos")
elif idade >= 15 and idade <= 21 and sexo.lower() == "masculino nao atleta":
    print("livros, jardinagem e eletrodomesticos")
elif idade >=22 and idade <= 32 and sexo.lower() == "feminino":
    print("artigos esportivos e itens de casa")
else:
    print("erro")
    