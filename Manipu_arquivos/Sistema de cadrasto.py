opcoes = input("Digite uma dessas opções: \n1)Criar uma conta \n2) Já tenho uma conta \n ")

if opcoes.lower() in ("1", "criar uma conta", "criar conta"):
    with open("cadrastos.txt", "a") as cadastro:
         criar_email = input("Digite o nome do email que deseja, exemplo (cleito.silva@gmail.com): ")
         criar_senha = input("Digite a senha que deseja, (lembre-se: Sua senha tem que ser forte): ")
         cadastro.write("Email cadastrado: " + criar_email + "\n")
         cadastro.write("Senha: " + criar_senha + "\n\n") 

elif opcoes.lower() in ("2", "já tenho uma conta", "já tenho", "ja tenho"):
         try:
            with open("cadastros.txt", "r", encoding="utf-8") as cadastrados:
                print(cadastrados.read())
         except FileNotFoundError:
            print("Nenhum cadastro encontrado.")

else:
    print("Opção inválida, tente novamente.")