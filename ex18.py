salario = int(float("digite seu salario: "))
horas_extras = int (input("digite suas horas extras:"))
valor = int(float("digite o valor da hora extra:"))

if salario >= 0:
    salario = salario + (horas_extras * valor)
    print (f"seu salario e {salario}")
else:
    print ("salario invalido")

 