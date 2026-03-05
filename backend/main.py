from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from backend.core.config import settings
from backend.db.database import engine, Base
import backend.db.models
from backend.api_v1.routes import auth, users, dashboard, post_harvest, leaf_scan, chatbot, budget, yield_predict, fertilizer, disease, crop_recommend, market

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Smart Farming & Post-Harvest Assistant API",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Create tables on startup
@app.on_event("startup")
def configure_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Database creation error: {e}")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        location = " -> ".join(map(str, error["loc"]))
        errors.append(f"{location}: {error['msg']}")
    return JSONResponse(
        status_code=422,
        content={"status": "error", "error": "; ".join(errors)}
    )

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "error": str(exc.detail)}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=200,  # FORCE 200 to bypass Vercel's strict 500 interception
        content={"status": "error", "error": str(exc)}
    )

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development. Can restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["auth"])
app.include_router(users.router, prefix=f"{settings.API_V1_STR}/users", tags=["users"])
app.include_router(dashboard.router, prefix=f"{settings.API_V1_STR}/dashboard", tags=["dashboard"])
app.include_router(post_harvest.router, prefix=f"{settings.API_V1_STR}/post-harvest", tags=["post-harvest"])
app.include_router(leaf_scan.router, prefix=f"{settings.API_V1_STR}/leaf-scan", tags=["leaf-scan"])
app.include_router(chatbot.router, prefix=f"{settings.API_V1_STR}/chatbot", tags=["chatbot"])
app.include_router(budget.router, prefix=f"{settings.API_V1_STR}/budget", tags=["budget"])
app.include_router(yield_predict.router, prefix=f"{settings.API_V1_STR}/yield", tags=["yield"])
app.include_router(fertilizer.router, prefix=f"{settings.API_V1_STR}/fertilizer-recommendation", tags=["fertilizer"])
app.include_router(disease.router, prefix=f"{settings.API_V1_STR}/disease-advisory", tags=["disease"])
app.include_router(crop_recommend.router, prefix=f"{settings.API_V1_STR}/crop-recommendation", tags=["crop_recommend"])
app.include_router(market.router, prefix=f"{settings.API_V1_STR}/market-price", tags=["market"])

# Mount uploads directory for static file serving
from fastapi.staticfiles import StaticFiles
import os

# Static serving (Adjust for Vercel /tmp)
static_dir = "/tmp/uploads" if os.name != 'nt' else "uploads"
if not os.path.exists(static_dir):
    try:
        os.makedirs(static_dir, exist_ok=True)
    except:
        pass

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")
else:
    # Fallback to local uploads if /tmp failed or we're building
    try:
        os.makedirs("uploads", exist_ok=True)
        app.mount("/static", StaticFiles(directory="uploads"), name="static")
    except:
        pass # Ignore if read-only

# Mount frontend directory
try:
    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend") if '__file__' in locals() else os.path.join(os.getcwd(), "..", "frontend")
    if os.path.exists(frontend_dir):
        app.mount("/app", StaticFiles(directory=frontend_dir, html=True), name="frontend")
except Exception:
    pass


@app.get("/")
def read_root():
    return {"message": "Kisan Saathi API - SYNC CHECK 1007"}
