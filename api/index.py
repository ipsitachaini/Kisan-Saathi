import sys
import os
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

# Root of the repo
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

try:
    # Try to import the real app
    from backend.main import app
except Exception as e:
    # If it fails, report the error properly
    app = FastAPI()
    
    error_data = {
        "status": "error",
        "message": "Backend initialization failed - Critical Diagnostic V3",
        "cache_breaker_id": "1805_SYNC",
        "error_type": type(e).__name__,
        "error_msg": str(e),
        "traceback": traceback.format_exc(),
        "sys_path": sys.path
    }
    
    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def fallback(request: Request, path: str = ""):
        return JSONResponse(status_code=500, content=error_data)
