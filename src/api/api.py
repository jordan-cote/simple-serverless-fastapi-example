from fastapi import APIRouter

from .endpoints import user

router = APIRouter()
router.include_router(user.router, prefix="/user", tags=["Users"])
