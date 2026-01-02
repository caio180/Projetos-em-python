opcoes = input("Digite a opção desejada: \n1) Adicionar contatos \n2) Listar contatos \n3) Buscar um contato \n4) Remover contato \nOpção desejada: ")

if opcoes.lower() in ("1", "adicionar", "adicionar contatos", "add"):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número do telefone: ")

    with open("agenda_contatos.csv", "a") as arquivo:
        arquivo.write(f"Nome: {nome} Telefone: {telefone}\n")
        print(f"Contato {nome}, adicionado com sucesso.")
elif opcoes.lower() in ("2", "listar", "listar contatos"):
  try: 
     with open("agenda_contatos.csv", "r") as arquivo:
        contatos_salvos = arquivo.readline()
        if len(contatos_salvos) == 0:
            print("Agenda fazia")
        else:
            for linha in contatos_salvos:
                contatos_salvos.strip()
                print(f"Contatos salvos: {contatos_salvos}")
  except FileNotFoundError:
      print("Nenhum contato encontrado.")
  
elif opcoes.lower() in ("3", "buscar contatos", "buscar"):
    busca = input("Digite o nome do contado: ")
    with open("agenda_contatos.csv", "r") as arquivo:
        contatos_salvos = arquivo.read()
        print(f"O nome {busca} é: {busca in contatos_salvos}")