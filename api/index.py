import sys
import os
import traceback

# Root of the repo
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
backend = os.path.join(root, 'backend')

if root not in sys.path:
    sys.path.insert(0, root)
if backend not in sys.path:
    sys.path.insert(0, backend)

try:
    from backend.main import app
except Exception as e:
    from fastapi import FastAPI, Request
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    error_data = {
        "status": "error",
        "message": "Critical startup failure",
        "error": str(e),
        "traceback": traceback.format_exc(),
        "sys_path": sys.path
    }
    
    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def catch_all(request: Request, path: str = ""):
        return JSONResponse(status_code=200, content=error_data)
