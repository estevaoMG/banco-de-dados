import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("DELETE FROM clientes WHERE id = 8")
    conexao.commit()
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)",
        ("Teste 3", "teste3@gmail.com"),
    )
    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?,?, ?)",
        (2, "Teste 4", "teste4@gmail.com"),
    )
    conexao.commit()
except Exception as exc:
    print(f"Ops! Um erro ocorreu! {exc}")
    conexao.rollback()
