media1,media2,media3, nota=float(input("insira a 1 media")), float(input("insira a 2 media")), float(input("insira a 3 media")), int(input("insira a nota: "))

if nota <= 2:
    media1 = nota
    print("o aluno esta reprovado")
elif nota <=5:
    media2 = nota
    print("o aluno esta de recuperação")
else:
    media3 = nota >=7
    print("o aluno esta aprovado")