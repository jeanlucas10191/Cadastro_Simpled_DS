while True:
    print("\n===========================")
    print("    SISTEMA DE CADASTRO")
    print("===========================")
    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Pesquisar usuario")
    print("4 - Listar usuarios")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")

    # Ccadastro
    if opcao == "1":
        print("\n==== TELA DE CADASTRO ====")

        nome = input("Digite seu nome: ").strip()

        arquivo = open("usuarios.txt", "a+")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        existe = False

        for usuario in usuarios:
            dados = usuario.strip().split(";")
            if dados[0] == nome:
                existe = True

        if existe:
            print("Esse usuario ja existe!")
        else:
            senha = input("Crie sua senha: ")

            arquivo = open("usuarios.txt", "a")
            arquivo.write(nome + ";" + senha + "\n")
            arquivo.close()
        else:
            curso = input("Informe seu curso")
            arquivo

            print("Cadastro realizado com sucesso!")

    # FAZER LOGIN
    elif opcao == "2":
        print("\n====== TELA DE LOGIN ======")

        nome = input("Digite seu nome: ").strip()
        senha = input("Digite sua senha: ")

        arquivo = open("usuarios.txt", "a+")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        logado = False

        for usuario in usuarios:
            dados = usuario.strip().split(";")

            if len(dados) == 2:
                if dados[0] == nome and dados[1] == senha:
                    logado = True

        if logado:
            print("Login realizado com sucesso!")
            print("Bem-vindo,", nome)
        else:
            print("Nome ou senha incorretos!")

    # PESQUISAR USUARIO
    elif opcao == "3":
        print("\n==== PESQUISAR USUARIO ====")

        pesquisa = input("Digite o nome para pesquisar: ").strip()

        arquivo = open("usuarios.txt", "a+")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        encontrado = False

        for usuario in usuarios:
            dados = usuario.strip().split(";")

            if len(dados) == 2:
                if pesquisa.lower() in dados[0].lower():
                    print("Usuario encontrado:", dados[0])
                    encontrado = True

        if not encontrado:
            print("Usuario nao encontrado!")

    # LISTAR USUARIOS
    elif opcao == "4":
        print("\n==== USUARIOS CADASTRADOS ====")

        arquivo = open("usuarios.txt", "a+")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        if len(usuarios) == 0:
            print("Nenhum usuario cadastrado.")
        else:
            for usuario in usuarios:
                dados = usuario.strip().split(";")

                if len(dados) == 2:
                    print("-", dados[0])

    # SAIR
    elif opcao == "5":
        print("Voce saiu do sistema!")
        break

    else:
        print("Opcao invalida!")