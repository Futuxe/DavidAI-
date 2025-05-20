from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from datetime import datetime, timedelta
from jose import jwt

# === Konfiguracja bazy danych ===
DATABASE_URL = "sqlite:///./davidai.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Tworzy tabele jeśli nie istnieją
Base.metadata.create_all(bind=engine)

# === Funkcja do pobierania sesji DB ===
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === JWT Tokeny ===
SECRET_KEY = "supersecret"  # możesz zamienić na zmienną środowiskową
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
