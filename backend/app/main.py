from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.agent import router as agent_router
from app.config import settings
from app.database import Base, engine
from app.models.interaction import HCPInteraction
from app.routes.interactions import router as interactions_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(interactions_router)
app.include_router(agent_router)


@app.get("/")
def root():
    return {
        "message": "AI First CRM HCP Backend is running",
        "version": settings.APP_VERSION
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME
    }