from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.db.session import get_session
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])

# 新增用户
@router.post("/add", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# 查询所有用户
@router.get("/list", response_model=list[User])
def read_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()

# 查询单个用户
@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户未找到")
    return user

# 更新用户
@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户未找到")

    for field, value in updated_user.dict(exclude_unset=True).items():
        setattr(user, field, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# 删除用户
@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="用户未找到")
    session.delete(user)
    session.commit()
    return {"message": "用户已删除"}
