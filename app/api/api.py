from fastapi import APIRouter

from app.api.endpoints import items, login, users

api_router = APIRouter()
@api_router.get("/health-check")
def root_api():
    return {"status": "ok"}

api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
