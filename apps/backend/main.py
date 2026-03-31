from fastapi import FastAPI, APIRouter

app = FastAPI()

api_router = APIRouter(prefix="/api")

@api_router.get("/health")
def check_health():
    return {"status": "ok"}

app.include_router(api_router)