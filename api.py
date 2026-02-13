from fastapi import FastAPI
from pydantic import BaseModel
from database import get_connection

app = FastAPI(title="API de Pessoas", version="1.0.0")


# =========================
# MODELO DE DADOS
# =========================
class Pessoa(BaseModel):
    nome: str
    idade: int
    cidade: str


# =========================
# ROTA RAIZ
# =========================
@app.get("/")
def raiz():
    return {"mensagem": "API rodando com sucesso 🚀"}


# =========================
# GET - LISTAR PESSOAS
# =========================
@app.get("/pessoas")
def listar_pessoas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()

    conn.close()

    return [dict(pessoa) for pessoa in pessoas]


# =========================
# POST - CRIAR PESSOA
# =========================
@app.post("/pessoas")
def criar_pessoa(pessoa: Pessoa):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pessoas (nome, idade, cidade)
        VALUES (?, ?, ?)
    """, (pessoa.nome, pessoa.idade, pessoa.cidade))

    conn.commit()
    conn.close()

    return {"mensagem": "Pessoa criada com sucesso"}


# =========================
# PUT - ATUALIZAR PESSOA
# =========================
@app.put("/pessoas/{pessoa_id}")
def atualizar_pessoa(pessoa_id: int, pessoa: Pessoa):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE pessoas
        SET nome = ?, idade = ?, cidade = ?
        WHERE id = ?
    """, (pessoa.nome, pessoa.idade, pessoa.cidade, pessoa_id))

    conn.commit()
    conn.close()

    return {"mensagem": "Pessoa atualizada com sucesso"}


# =========================
# DELETE - REMOVER PESSOA
# =========================
@app.delete("/pessoas/{pessoa_id}")
def deletar_pessoa(pessoa_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM pessoas
        WHERE id = ?
    """, (pessoa_id,))

    conn.commit()
    conn.close()

    return {"mensagem": "Pessoa removida com sucesso"}
