import sqlite3

banco = sqlite3.connect("cadastros.db")
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL        
                )""")

opcoes = input("Digite a opção desejada: \n1) Criar uma conta \n2) Fazer login \n= ")

if opcoes.lower() in ("1", "criar conta"):
    email = input("Crie um email, exemplo (claudio.silva@gmail.com): \n= ")
    senha = input("Crie uma senha, de preferencia forte, minímo 8 caracteres: \n= ")
    if len(senha) < 8:
        print("Error, a senha precisa de no mínimo 8 caracteres, tente novamente.")
    else:
        try:
            cursor.execute("""
            INSERT INTO usuarios (email, senha)
            VALUES (?, ?)
        """, (email, senha))
            banco.commit()
            print("Conta criada com sucesso!!")
        except sqlite3.IntegrityError:
            print("Erro: esse email já está cadastrado.")
elif opcoes.lower() in ("2", "fazer login"):
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    cursor.execute("""  
        SELECT * FROM usuarios WHERE email = ? AND senha = ?
                   
                """, (email, senha))
    
    if cursor.fetchone():
        print("Login realizado com sucesso!!")
    else:
        print("ERRO: email ou senha incorretos.") 

cursor.close()
banco.close()

