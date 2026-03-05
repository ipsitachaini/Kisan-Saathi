from fastapi import FastAPI
app = FastAPI()
@app.get("/api/final-check")
async def final_check():
    return {"message": "FINAL_CHECK_SUCCESS"}

@app.get("/{path:path}")
async def catch_all(path: str):
    return {"message": "CATCH_ALL", "path": path}
