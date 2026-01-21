import sentry_sdk
from fastapi import FastAPI
from app.core.config import settings

if settings.SENTRY_DSN:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
)

@app.get("/")
async def root():
    return {"message": "Welcome to Al-Huda API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
