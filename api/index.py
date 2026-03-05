import sys
import os
import traceback
import json

# Add root to sys.path
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if root not in sys.path:
    sys.path.insert(0, root)

try:
    # Try to import the app
    from backend.main import app
except Exception as e:
    # If it fails, create a dummy app to report the error
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    error_info = {
        "status": "error",
        "message": "Backend initialization failed",
        "error": str(e),
        "traceback": traceback.format_exc(),
        "cwd": os.getcwd(),
        "sys_path": sys.path
    }
    
    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def error_handler(path: str = ""):
        return JSONResponse(status_code=200, content=error_info)
