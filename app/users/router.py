from datetime import time
from fastapi import APIRouter, Depends, HTTPException, Response, status
from app.users.auth import authenticate_user, create_access_token, get_password_hash, verify_password
from app.users.dependencies import get_current_admin_user, get_current_user
from app.users.models import Users
from app.users.schemas import SUserAuth, SUserRegister
from app.users.repository import UserRepository
from app.users.models import User_role


router = APIRouter(
    prefix="/auth",
    tags = ["Auth & Users"]   
)

@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserRepository.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    new_user_id =  await UserRepository.add(name = user_data.name,surname = user_data.surname, email=user_data.email, password=hashed_password, role = User_role.user)
    
    await UserRepository.add_new_cart(new_user_id)
    
     
@router.post("/login")
async def login_user(response: Response,user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.user_id)})
    response.set_cookie("login_access_token", access_token, httponly = True)
    return {"access_token":access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("login_access_token")


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
  return current_user


@router.get("/all")
async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
  return await UserRepository.find_all()



