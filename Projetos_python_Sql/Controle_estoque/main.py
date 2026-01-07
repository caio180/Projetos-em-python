import sqlite3
import time

banco = sqlite3.connect("registro.db")
cursor = banco.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT,
    preco REAL           
               )""")

while True:
    opcoes = input("Digite a opção desejada: \n1) Adicionar um produto e o preço dele. \n2) Listar os produtos. \n3) Calcular todos os preços. \nCaso deseja parar o programa digite 0. \nEscolha a opção: ")
    if opcoes.lower() in ("1", "adicionar produto"):
        nome_produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        cursor.execute(
            "INSERT INTO estoque (produto, preco) VALUES (?, ?)",
            (nome_produto, preco)
        )     
        banco.commit()
        print("Produto adicionado com sucesso")

    elif opcoes.lower() in ("2", "listar produto"):
         cursor.execute("SELECT id, produto, preco FROM estoque")
         produtos = cursor.fetchall()
         if not produtos:
            print("Nenhum produto cadastrado.")
         else:
            print("\nLista de produtos:")
            for id, produto, preco in produtos:
                print(f"ID: {id} | Produto: {produto} | Preço: R$ {preco}")

    elif opcoes.lower() in ("3", "somar os preços"):
         cursor.execute("SELECT SUM(preco) FROM estoque")
         total = cursor.fetchone()[0]

         if total is None:
            print("Nenhum produto cadastrado.")
         else:
            print(f"Valor total do estoque: R$ {total}")

    elif opcoes == "0":
        print("Encerrando programa...")
        time.sleep(3)
        break

    else:
        print("Opção inválida.")

cursor.close()
banco.close()