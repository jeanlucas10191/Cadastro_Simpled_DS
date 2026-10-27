
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

            if len(dados) == 4 and dados[0].lower() == nome.lower():
                existe = True
                break

            # Compatibilidade com cadastros antigos
            if len(dados) == 3 and dados[0].lower() == nome.lower():
                existe = True
                break

        if existe:
            print("Esse usuario ja existe!")
        else:
            senha = input("Crie sua senha: ").strip()
            idade = input("Digite sua idade: ").strip()
            curso = input("Digite o curso do aluno: ").strip()

            if senha == "" or idade == "" or curso == "":
                print("Senha, idade e curso nao podem ficar vazios!")
            elif not idade.isdigit() or int(idade) <= 0:
                print("Idade invalida! Digite uma idade valida.")
            else:
                arquivo = open("usuarios.txt", "a", encoding="utf-8")
                arquivo.write(
                    nome + ";" + senha + ";" + idade + ";" + curso + "\n"
                )
                arquivo.close()

                print("Cadastro realizado com sucesso!")

    # FAZER LOGIN COM 3 TENTATIVAS
    elif opcao == "2":
        print("\n====== TELA DE LOGIN ======")

        arquivo = open("usuarios.txt", "a+", encoding="utf-8")
        arquivo.seek(0)
        usuarios = arquivo.readlines()
        arquivo.close()

        tentativas = 3
        logado = False
        usuario_logado = None

        while tentativas > 0 and not logado:
            print("\nTentativas restantes:", tentativas)

            nome = input("Digite seu nome: ").strip()
            senha = input("Digite sua senha: ").strip()

            for usuario in usuarios:
                dados = usuario.strip().split(";")

                if len(dados) == 4:
                    if dados[0].lower() == nome.lower() and dados[1] == senha:
                        logado = True
                        usuario_logado = dados
                        break

                # Aceitar cadastros antigos sem idade
                elif len(dados) == 3:
                    if dados[0].lower() == nome.lower() and dados[1] == senha:
                        logado = True
                        usuario_logado = dados
                        break

            if not logado:
                tentativas -= 1

                if tentativas > 0:
                    print("Nome ou senha incorretos!")
                    print("Voce ainda tem", tentativas, "tentativa(s).")
                else:
                    print("\nVoce errou as 3 tentativas!")
                    print("Voltando ao menu principal...")

        # MENU DO USUARIO LOGADO
        if logado:
            while True:
                print("\n==================")
                print("===Tela de usuario===")
                print("==================")
                print("Bem-vindo,", usuario_logado[0])
                print("\n1 - Ver meus dados")
                print("2 - Sair do login")

                opcao_usuario = input("Escolha uma opcao: ").strip()

                # VER DADOS DO USUARIO LOGAD  O
                if opcao_usuario == "1":
                        print("\n==================")
                        print("=== MEUS DADOS ===")
                        print("==================")
                        print("Nome:", usuario_logado[0])

                        if len(usuario_logado) == 4:
                            print("Idade:", usuario_logado[2])
                            print("Curso:", usuario_logado[3])
                        else:
                            print("Idade: Nao informada (cadastro antigo)")
                            print("Curso:", usuario_logado[2])

                        input("\nPressione ENTER para voltar...")

                # SAIR DO LOGIN
                elif opcao_usuario == "2":
                    print("Voce saiu da sua conta!")
                    break

                else:
                    print("Opcao invalida! Digite 1 ou 2.")

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

            if len(dados) == 4:
                if pesquisa.lower() in dados[0].lower():
                    print("\nUsuario encontrado:", dados[0])
                    print("Idade:", dados[2])
                    print("Curso:", dados[3])
                    encontrado = True

            elif len(dados) == 3:
                if pesquisa.lower() in dados[0].lower():
                    print("\nUsuario encontrado:", dados[0])
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

            if len(dados) == 4:
                print("---------------------------")
                print("Nome:", dados[0])
                print("Idade:", dados[2])
                print("Curso:", dados[3])
                encontrou = True

            elif len(dados) == 3:
                print("---------------------------")
                print("Nome:", dados[0])
                print("Curso:", dados[2])
                encontrou = True

        if not encontrou:
            print("Nenhum aluno cadastrado.")

    # SAIR DO SISTEMA
    elif opcao == "5":
        print("Voce saiu do sistema!")
        break