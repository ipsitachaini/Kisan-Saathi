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
    # BUILD_MARKER: 2045_RESTORED_DIAGNOSTIC
    from backend.main import app
except Exception as e:
    # DIAGNOSTIC MODE ACTIVE - RESTORED
    app = FastAPI()
    
    # Collect as much info as possible
    error_data = {
        "status": "error",
        "message": "Backend initialization failed - Diagnostic RESTORED V6",
        "error_type": type(e).__name__,
        "error_msg": str(e),
        "traceback": traceback.format_exc(),
        "sys_path": sys.path,
        "sys_version": sys.version,
        "python_executable": sys.executable,
        "cwd": os.getcwd(),
        "files_in_cwd": os.listdir(".") if os.path.exists(".") else "N/A",
        "backend_exists": os.path.exists(os.path.join(root, "backend")),
        "env_keys": list(os.environ.keys())

    }
    
    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def fallback(request: Request, path: str = ""):
        return JSONResponse(status_code=200, content=error_data)

