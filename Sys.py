import bancodedadosefuncoes as fn
import json
import sys

try:
    with open("usuarios.json", "r") as arquivo:
        fn.banco_usuarios = json.load(arquivo)
except FileNotFoundError:
    pass


while True:

    if fn.tentativas == 3:
        print("="*10)
        print("Você será desconectado. TYPE: Suspeita de SPAM.")
        print("="*10)
        break

    print("\n -- SISTEMA DE LOGIN/CADASTRO --")
    try:
        opcao = int(input("\n1 - Login \n2 - Cadastrar Usuário \n3 - Sair \n4 - Conferir hora e data \n5 - Conferir banco de dados (liberado para teste) \n -- ESCOLHA: "))

        if opcao == 1:
            nomelog = input("Digite seu usuário cadastrado: ").strip()
            
            encontrado = False

            for c in fn.banco_usuarios:
                    if nomelog == c['usuario']:
                        encontrado = True
                        senhalog = input("Digite sua senha: ").strip()
                        if senhalog == c['senha']:
                            print("Acesso liberado!")
                        else:
                            print("Senha incorreta!")
                            fn.tentativas += 1
                            print(f"{fn.tentativas}/3 tentativas")
                            break

            if not encontrado:
                    print("="*10)
                    print("Usuário não encontrado!")

        elif opcao == 2:
            while True:
                    
                criaruser = input("Crie um novo usuário: ").strip()
                usuario_existe = False

                for i in fn.banco_usuarios:
                    if criaruser == i['usuario']:
                            usuario_existe = True
                            break

                if usuario_existe:
                    print("Usuário já cadastrado!")
                else:
                    criarsenha = input("Crie uma nova senha: ").strip()
                    novo_usuario = {"usuario": criaruser, "senha": criarsenha}
                    fn.banco_usuarios.append(novo_usuario)

                    with open("usuarios.json", "w") as arquivo:
                        json.dump(fn.banco_usuarios, arquivo, indent=4)

                    print("Usuário criado com sucesso!")
                    print("-"*10)
                    input("Digite ENTER PARA CONTINUAR: ")
                    fn.limpar_tela()
                    break

        elif opcao == 3:
            fn.sair()
            break
        
        elif opcao == 4:
                if sys.stdin.isatty():
                    sys.stdin.flush()

                print(f"ATT: {fn.mostrardataehora()} - Horário de Brasília")

                input("\nPressione ENTER para limpar a tela e voltar ao menu: ")
                fn.limpar_tela()

        elif opcao == 5:

            if sys.stdin.isatty():
                sys.stdin.flush()

            print(f"\n == BANCO DE DADOS | Relatório: {fn.mostrardataehora()} - Brasília, Brasil. ==")

            for i in fn.banco_usuarios:
                print(f"User: {i['usuario']:<15} | Senha: {i['senha']}")
            input("\nPressione ENTER para limpar a tela e voltar ao menu: ")
            fn.limpar_tela()

    except Exception as e:
        print(f"\n[SISTEMA] Ocorreu um erro inesperado: {e}")
        input("Pressione ENTER para tentar novamente...")

    except ValueError:
        print("="*10)
        print("ERRO!")
        print("="*10)

    except IndexError:
        print("Digite uma opção válida!")
