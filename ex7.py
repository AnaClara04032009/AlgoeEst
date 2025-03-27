numero1,numero2,operacao=int(input("insira o 1 numero")), int(input("insira o 2 numero")), input("insira a "
"operacao:")
if operacao== "+" or operacao=='adicao' or operacao== "mais":
    print(numero1+numero2)
elif operacao== "-"or operacao== 'subtracao' or operacao=="menos":
    print(numero1+numero2)
elif operacao== "*" or operacao =='multiplicacao'or operacao== "vezes":
    print(numero1*numero2)
elif operacao== "/" or operacao== 'divisao':
    print(numero1/numero2)
else:
    print("operacao invalida")
 
