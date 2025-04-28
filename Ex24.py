numeros= []
for i in range(5): 
    numero=int(input("Digite um número"))
    numeros.append(numero)

maior= numeros[0]
menor=numeros[0]
for numero in numeros:
    if numero>maior:
        maior=numero
    if numero<menor:
        menor=numero
    print("Maior número:",maior)
    print("Menor número:",menor)