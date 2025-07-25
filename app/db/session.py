from sqlmodel import create_engine, Session
from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=False,             # 生产环境关闭SQL打印
    pool_size=5,            # 连接池大小
    max_overflow=10,        # 允许的最大溢出连接数
    pool_timeout=30,        # 连接超时时间（秒）
    pool_pre_ping=True,     # 检查连接有效性
    pool_recycle=3600       # 每小时回收连接，防止超时
)

def get_session():
    with Session(engine) as session:
        yield session
