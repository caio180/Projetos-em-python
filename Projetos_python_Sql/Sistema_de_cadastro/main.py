import sqlite3
import bcrypt

def gerar_hash(senha):
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

banco = sqlite3.connect("cadastros.db")
cursor = banco.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    email TEXT UNIQUE NOT NULL,
    senha BLOB NOT NULL
)
""")


opcoes = input("Digite a opção desejada: \n1) Criar uma conta \n2) Fazer login \n3) Alterar senha \n4) Excluir cadastro \n= ")

if opcoes.lower() in ("1", "criar conta"):
    email = input("Crie um email, exemplo (claudio.silva@gmail.com): \n= ")
    senha = input("Crie uma senha, de preferencia forte, minímo 8 caracteres: \n= ")

    if len(senha) < 8:
        print("Error, a senha precisa de no mínimo 8 caracteres, tente novamente.")
    else:
        senha_hash = gerar_hash(senha)
        try:
            cursor.execute("""
            INSERT INTO usuarios (email, senha)
            VALUES (?, ?)
        """, (email, senha_hash))
            banco.commit()
            print("Conta criada com sucesso !!")
        except sqlite3.IntegrityError:
            print("Erro: esse email já está cadastrado.")

elif opcoes.lower() in ("2", "fazer login"):
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    cursor.execute("""
        SELECT senha FROM usuarios WHERE email = ?
    """, (email))

    resultado = cursor.fetchone()

    if resultado and bcrypt.checkpw(senha.encode(), resultado[0]):
        print("Login realizado com sucesso !")
    else:
        print("ERRO: email ou senha incorretos.")


elif opcoes.lower() in ("3", "alterar senha"):
    email = input("Digite seu email: ")
    senha_atual = input("Digite sua senha atual: ")
    
    cursor.execute("""
        SELECT senha FROM usuarios WHERE email = ?
    """, (email))

    resultado = cursor.fetchone()

    if resultado and bcrypt.checkpw(senha_atual.encode(), resultado[0]):
        nova_senha = input("Digite uma nova senha: ")

        if len(nova_senha) < 8:
            print("Erro: a senha precisa de no mínimo 8 caracteres.")
        else:
            nova_senha_hash = gerar_hash(nova_senha)
            cursor.execute("""
                UPDATE usuarios
                SET senha = ?
                WHERE email = ?
            """, (nova_senha_hash, email))
            banco.commit()
            print("Senha alterada com sucesso!")
    else:
        print("Email ou senha incorretos.")

elif opcoes.lower() in ("4", "excluir"):

    id_usuario = input("Digite o id do seu usuário: ")
    cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id_usuario))
    usuarios_cadastrados = cursor.fetchall()


cursor.close()
banco.close()     