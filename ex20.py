idade = int(input("insira sua idade"))  
membro = input("voce e membro do clube? (sim ou nao)")

if idade >=18 and membro.lower() == "sim":
    print("voce pode entrar no clube")
elif idade >=18 and membro.lower() == "nao":
    print("voce nao pode entrar no clube")
elif membro.lower() == "sim":
    print("voce e um membro do clube")  
else:
    print("voce nao pode entrar no clube")
