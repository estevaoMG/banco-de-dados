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


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


cliente = recuperar_cliente(cursor, 2)
print(cliente)

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)

# dados = [
#     ("Guilherme", "guilherme@gmail.com"),
#     ("Chappie", "chappie@gmail.com"),
#     ("Melaine", "melaine@gmail.com"),
# ]
# inserir_muitos(conexao, cursor, dados)
