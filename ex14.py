nome_de_usuario  = input("insira o nome de usuario")
senha = int(input("insira senha"))

if nome_de_usuario == "admin":
    print ("cadastrado com sucesso {nome_de_usuario}, {senha} senha")
else:
    print("erro no cadastro tente novamente")