import sys
import os
import traceback
import json

# Absolute path to the project root
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

try:
    # Try to import the app from backend.main
    from backend.main import app
except Exception as e:
    # If initialization fails, create a fail-safe app to report the error
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    backend_path = os.path.join(root, 'backend')
    
    error_info = {
        "status": "error",
        "message": "Backend initialization failed - DIAGNOSTICS ACTIVE",
        "error": str(e),
        "traceback": traceback.format_exc(),
        "root_exists": os.path.exists(root),
        "backend_exists": os.path.exists(backend_path),
        "root_contents": os.listdir(root) if os.path.exists(root) else [],
        "sys_path": sys.path
    }
    
    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def fallback_handler(path: str = ""):
        return JSONResponse(status_code=200, content=error_info)
