
while True:
    print("\n===========================")
    print("     SISTEMA DE CADASTRO")
    print("===========================")
    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - Pesquisar usuario")
    print("4 - Mostrar dados cadastrados")
    print("5 - Sair")

    opcao = input("Escolha uma opcao (1 a 5): ").strip()

    # VALIDAR OPCAO
    if opcao not in ["1", "2", "3", "4", "5"]:
        print("Opcao invalida! Digite somente um numero de 1 a 5.")
        continue

    # CADASTRAR ALUNO
    if opcao == "1":
        print("\n==== TELA DE CADASTRO ====")

        nome = input("Digite seu nome: ").strip()

        if nome == "":
            print("Nome invalido!")
            continue

        arquivo = open("usuarios.txt", "a+", encoding="utf-8")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        existe = False

        for usuario in usuarios:
            dados = usuario.strip().split(";")

            if len(dados) == 3 and dados[0].lower() == nome.lower():
                existe = True
                break

        if existe:
            print("Esse usuario ja existe!")
        else:
            senha = input("Crie sua senha: ").strip()
            curso = input("Digite o curso do aluno: ").strip()

            if senha == "" or curso == "":
                print("Senha e curso nao podem ficar vazios!")
            else:
                arquivo = open("usuarios.txt", "a", encoding="utf-8")
                arquivo.write(nome + ";" + senha + ";" + curso + "\n")
                arquivo.close()

                print("Cadastro realizado com sucesso!")

    # FAZER LOGIN
    elif opcao == "2":
        print("\n====== TELA DE LOGIN ======")

        nome = input("Digite seu nome: ").strip()
        senha = input("Digite sua senha: ").strip()

        arquivo = open("usuarios.txt", "a+", encoding="utf-8")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        logado = False

        for usuario in usuarios:
            dados = usuario.strip().split(";")

            if len(dados) == 3:
                if dados[0].lower() == nome.lower() and dados[1] == senha:
                    logado = True
                    break

        if logado:
            print("Login realizado com sucesso!")
            print("Bem-vindo,", nome)
        else:
            print("Nome ou senha incorretos!")

    # PESQUISAR USUARIO
    elif opcao == "3":
        print("\n==== PESQUISAR USUARIO ====")

        pesquisa = input("Digite o nome para pesquisar: ").strip()

        arquivo = open("usuarios.txt", "a+", encoding="utf-8")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        encontrado = False

        for usuario in usuarios:
            dados = usuario.strip().split(";")

            if len(dados) == 3:
                if pesquisa.lower() in dados[0].lower():
                    print("Usuario encontrado:", dados[0])
                    print("Curso:", dados[2])
                    encontrado = True

        if not encontrado:
            print("Usuario nao encontrado!")

    # MOSTRAR DADOS CADASTRADOS
    elif opcao == "4":
        print("\n==== DADOS CADASTRADOS ====")

        arquivo = open("usuarios.txt", "a+", encoding="utf-8")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        encontrou = False

        for usuario in usuarios:
            dados = usuario.strip().split(";")

            if len(dados) == 3:
                print("---------------------------")
                print("Nome:", dados[0])
                print("Curso:", dados[2])
                encontrou = True

        if not encontrou:
            print("Nenhum aluno cadastrado.")

    # SAIR
    elif opcao == "5":
        print("Voce saiu do sistema!")
        break

    else:
        print("Opcao invalida!")
