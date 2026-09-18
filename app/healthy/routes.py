from fastapi import APIRouter

router = APIRouter(prefix="/healthy", tags=["Healthy"])


@router.get("")
def healthy():
    return {"status": "healthy"}
