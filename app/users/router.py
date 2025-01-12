from fastapi import APIRouter, HTTPException, Response, status
from app.users.auth import authenticate_user, create_access_token, get_password_hash, verify_password
from app.users.schemas import SUserAuth, SUserRegister
from app.users.repository import UserRepository



router = APIRouter(
    prefix="/auth",
    tags = ["Auth & Пользователи"]   
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserRepository.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UserRepository.add(name = user_data.name,surname = user_data.surname, email=user_data.email, password=hashed_password)
    
    
@router.post("/login")
async def login_user(response: Response,user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.user_id})
    response.set_cookie("login_access_token", access_token, httponly = True)
    return {"access_token":access_token }


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjgsImV4cCI6MTczNjUyMjU0MX0.secoEkmKBkbW0EthLxvynuxk_-djDNqcYaM5ykc8ctI