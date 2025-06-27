from sqlmodel import create_engine, Session
from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=True,         # 控制是否打印 SQL 语句
    pool_pre_ping=True # 避免 MySQL 长时间连接中断
)

def get_session():
    with Session(engine) as session:
        yield session
