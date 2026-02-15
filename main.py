from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Pessoa
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Criar tabelas automaticamente
Base.metadata.create_all(bind=engine)

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# CRUD PESSOAS
# =========================

@app.post("/pessoas")
def criar_pessoa(pessoa: dict, db: Session = Depends(get_db)):
    nova = Pessoa(
        nome=pessoa["nome"],
        idade=pessoa["idade"],
        cidade=pessoa["cidade"]
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@app.get("/pessoas")
def listar_pessoas(db: Session = Depends(get_db)):
    return db.query(Pessoa).all()


@app.put("/pessoas/{pessoa_id}")
def atualizar_pessoa(pessoa_id: int, dados: dict, db: Session = Depends(get_db)):
    pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()

    if pessoa:
        pessoa.nome = dados["nome"]
        pessoa.idade = dados["idade"]
        pessoa.cidade = dados["cidade"]
        db.commit()
        db.refresh(pessoa)

    return pessoa


@app.delete("/pessoas/{pessoa_id}")
def deletar_pessoa(pessoa_id: int, db: Session = Depends(get_db)):
    pessoa = db.query(Pessoa).filter(Pessoa.id == pessoa_id).first()

    if pessoa:
        db.delete(pessoa)
        db.commit()

    return {"mensagem": "Pessoa removida com sucesso"}
