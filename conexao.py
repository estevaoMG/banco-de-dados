import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()


def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


atualizar_registro(conexao, cursor, "Guilherme Carvalho", "gui@gmail.com", 1)
atualizar_registro(conexao, cursor, "Giovanna Carvalho", "giovanna@gmail.com", 2)
