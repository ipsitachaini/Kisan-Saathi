from fastapi import FastAPI
from fastapi.responses import JSONResponse
import sys
import os
import traceback

app = FastAPI()

@app.get("/api/health")
async def health():
    backend_path = os.path.join(os.getcwd(), 'backend')
    return {
        "status": "ok",
        "python_version": sys.version,
        "cwd": os.getcwd(),
        "sys_path": sys.path,
        "backend_exists": os.path.exists(backend_path),
        "backend_files": os.listdir(backend_path) if os.path.exists(backend_path) else []
    }

@app.get("/api/test-import")
async def test_import():
    try:
        import backend.main
        return {"status": "success", "message": "backend.main imported successfully"}
    except Exception as e:
        return {
            "status": "error",
            "error_type": type(e).__name__,
            "message": str(e),
            "traceback": traceback.format_exc()
        }
