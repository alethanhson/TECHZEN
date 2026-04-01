from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.api import api_router
from app.core.config import settings
from app.db.base import engine, Base
from app.core.responses import setup_exception_handlers
from app.core.middleware import RateLimitMiddleware

from app.modules.user import models as _user_models
from app.modules.auth import models as _auth_models
from app.modules.product import models as _product_models

app = FastAPI(title=settings.PROJECT_NAME)
setup_exception_handlers(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RateLimitMiddleware, limit=20, window=60)
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix=settings.API_STR)

@app.get("/health")
def health_check():
    return {"status": "ok"}
