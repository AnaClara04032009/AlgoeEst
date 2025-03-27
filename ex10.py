valor = input("qual o valor da compra?")
if valor <= 100:
    print('nao ganha desconto')
elif valor >  50 and valor < 100 :
    print('a compra nao atingira o preco e nao ganhara desconto')
elif valor > 100 :
    print('ganhara 10 porcento de desconto na compra ')
else:
    print('valor invalida') 