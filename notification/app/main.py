"""Notification microservice - entry point.

Run:  python -m app.main
  or: uvicorn app.main:app --reload --port 8084
"""
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from py_eureka_client import eureka_client

from app.routers import notification

# Port lu depuis la variable d'environnement PORT (8084 par défaut)
PORT = int(os.getenv("PORT", "8084"))
EUREKA_SERVER = os.getenv("EUREKA_SERVER", "http://localhost:8761/eureka")
BASE_URL = f"http://localhost:{PORT}"

APP_NAME = "notification"
APP_VERSION = "1.0.0"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Démarrage : enregistrement dans Eureka avec les URL de santé et d'info
    await eureka_client.init_async(
        eureka_server=EUREKA_SERVER,
        app_name="NOTIFICATION",
        instance_host="localhost",
        instance_ip="127.0.0.1",
        instance_port=PORT,
        instance_id=f"localhost:notification:{PORT}",
        home_page_url=f"{BASE_URL}/",
        status_page_url=f"{BASE_URL}/info",
        health_check_url=f"{BASE_URL}/health",
    )
    print(f"Registered in Eureka as NOTIFICATION (port {PORT})")
    yield
    # Arrêt : désinscription d'Eureka
    await eureka_client.stop_async()
    print("Eureka client stopped")


app = FastAPI(
    title="Notification Microservice API",
    version=APP_VERSION,
    description=(
        "Notification microservice (Python / FastAPI, no database). "
        "Only the hello endpoint is implemented; the notification logic is to be developed by students."
    ),
    contact={"name": "Badia Abouhdid"},
    servers=[{"url": BASE_URL, "description": "Local"}],
    docs_url="/swagger-ui",       # Swagger UI
    openapi_url="/v3/api-docs",   # OpenAPI JSON
    redoc_url="/redoc",           # alternative documentation
    lifespan=lifespan,            # Eureka registration on startup / shutdown
)

app.include_router(notification.router)


# ---- Endpoints de santé et d'information ----
@app.get("/health", tags=["Monitoring"])
async def health():
    return {"status": "UP"}


@app.get("/info", tags=["Monitoring"])
async def info():
    return {
        "app": {
            "name": APP_NAME,
            "version": APP_VERSION,
            "description": "Microservice de gestion des notifications",
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)