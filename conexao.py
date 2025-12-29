import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# cursor.execute(
#     "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
# )

data = ("Giovanna", "gi@gmail.com")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
conexao.commit()
