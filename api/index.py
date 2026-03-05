import sys
import os
import traceback

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from backend.main import app
except Exception as e:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    @app.api_route("/{path_name:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
    async def catch_all(path_name: str):
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "Initialization failed",
                "error": str(e),
                "traceback": traceback.format_exc()
            }
        )
