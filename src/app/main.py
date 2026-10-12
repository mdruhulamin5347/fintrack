from fastapi import FastAPI

from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="Intelligent money management platform",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    
    # app.include_router(api_router,prefix="/api/v1")
    
    @app.get("/", include_in_schema=False)
    async def root():
        return {
            "app":settings.APP_NAME,
            "version":settings.APP_VERSION,
            "docs":"/docs" if False else "disabled",
        }
        
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        app_dir="src",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=settings.WORKERS,
    )