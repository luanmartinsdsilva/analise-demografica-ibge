from fastapi import APIRouter, HTTPException
from database import get_connection
from models import Pessoa

router = APIRouter()

@router.get("/pessoas")
def listar_pessoas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()

    conn.close()
    return [dict(pessoa) for pessoa in pessoas]


@router.get("/pessoas/{pessoa_id}")
def buscar_pessoa(pessoa_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pessoas WHERE id = ?", (pessoa_id,))
    pessoa = cursor.fetchone()
    conn.close()

    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    return dict(pessoa)


@router.post("/pessoas", status_code=201)
def criar_pessoa(pessoa: Pessoa):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pessoas (nome, idade, cidade)
        VALUES (?, ?, ?)
    """, (pessoa.nome, pessoa.idade, pessoa.cidade))

    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return {
        "id": novo_id,
        "nome": pessoa.nome,
        "idade": pessoa.idade,
        "cidade": pessoa.cidade
    }


@router.put("/pessoas/{pessoa_id}")
def atualizar_pessoa(pessoa_id: int, pessoa: Pessoa):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pessoas WHERE id = ?", (pessoa_id,))
    existente = cursor.fetchone()

    if not existente:
        conn.close()
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    cursor.execute("""
        UPDATE pessoas
        SET nome = ?, idade = ?, cidade = ?
        WHERE id = ?
    """, (pessoa.nome, pessoa.idade, pessoa.cidade, pessoa_id))

    conn.commit()
    conn.close()

    return {"mensagem": "Pessoa atualizada com sucesso"}


@router.delete("/pessoas/{pessoa_id}")
def deletar_pessoa(pessoa_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pessoas WHERE id = ?", (pessoa_id,))
    pessoa = cursor.fetchone()

    if not pessoa:
        conn.close()
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    cursor.execute("DELETE FROM pessoas WHERE id = ?", (pessoa_id,))
    conn.commit()
    conn.close()

    return {"mensagem": "Pessoa removida com sucesso"}
