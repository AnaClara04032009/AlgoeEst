notas=[]
for i in range(5):
    nota = float(input("digite a nota do aluno"))
    notas.append(nota)
media=sum(notas)/len(notas)

print("media das notas é",media)