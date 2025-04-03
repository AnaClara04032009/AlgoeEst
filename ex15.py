produto = input("digite o nome de um produto")
quantidade = int(input("insira a quatidade de produto"))
valor = float(input("digite o preço unitario do produto"))
total = float(input("digite o valor total da compra"))

if total>=100:
    desconto= total*0.05 
    print(f"o valor da compra e {total} , com o desconto o valor da compra fica {total - desconto}")
else:
    print("nao tera desconto pois o valor nao foi atingido")
