import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

nome = "Luan"

cursor.execute("""
SELECT nome, idade, cidade
FROM pessoas
WHERE nome = ?
""", (nome,))

resultado = cursor.fetchall()

for pessoa in resultado:
    print(pessoa)

conn.close()
