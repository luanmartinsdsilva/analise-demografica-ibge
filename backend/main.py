from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Pessoa, User
from fastapi.middleware.cors import CORSMiddleware
from auth import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

SECRET_KEY = "SUA_CHAVE_SUPER_SECRETA_AQUI"
ALGORITHM = "HS256"

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =========================
# REGISTER
# =========================
@app.post("/register")
def register(user: dict, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user["username"]).first()
    if existing:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    new_user = User(
        username=user["username"],
        hashed_password=hash_password(user["password"])
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Usuário criado com sucesso"}

# =========================
# LOGIN
# =========================
@app.post("/login")
def login(user: dict, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user["username"]).first()

    if not db_user or not verify_password(user["password"], db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": db_user.username})

    return {"access_token": token, "token_type": "bearer"}

# =========================
# PROTEÇÃO
# =========================
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
        return username
    except JWTError:
        raise HTTPException(status_code=401)

# =========================
# ROTAS PROTEGIDAS
# =========================
@app.get("/pessoas")
def listar_pessoas(user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Pessoa).all()

@app.post("/pessoas")
def criar_pessoa(pessoa: dict, user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    nova = Pessoa(**pessoa)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
