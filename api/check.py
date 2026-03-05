from fastapi import FastAPI
app = FastAPI()
@app.get("/api/check")
async def check():
    return {"status": "NEW_DEPLOYMENT_SUCCESS", "timestamp": "1805_SYNC"}
