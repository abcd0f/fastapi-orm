from typing import Optional
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    """用户模型类，表示系统中的用户实体。

    属性:
        id (Optional[int]): 用户的唯一标识符，主键，默认为None
        name (str): 用户的名称
        email (str): 用户的电子邮件地址
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
