#Exemplos básicos para não esquecer como funciona.
opcao = int(input("Escolha: \n1) Soma \n2 Subtrair"))

match opcao:
    case 1:
        print("Somar")
    case 2:
        print("Subtrair")
    case _:
        print("Opção inválida")