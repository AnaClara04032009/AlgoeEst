temperatura = float(input("digite a temperatura desejada:"))
if temperatura <= 20 :
    print ('frio')
elif temperatura > 20 and temperatura < 26 :
    print('morno')
elif temperatura >27:
    print ('quente')
else:
    print('temperatura invalida') 