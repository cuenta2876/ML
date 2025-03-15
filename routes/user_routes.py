from fastapi import APIRouter

router = APIRouter(prefix="/user")

@router.get("/")
def get_users():
    return {"message": "User routes placeholder"}