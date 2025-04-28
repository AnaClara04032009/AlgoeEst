palavras=[]
for i in range(5):
    palavra=input("digite uma palavra:")
    palavras.append(palavra)
palindromos=[]
for palavra in palavras:
    if palavra == palavra[::-1]:
        palindromos.append(palavra)
print("Palindromos:",palindromos)