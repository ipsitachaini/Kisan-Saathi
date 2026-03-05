from fastapi import FastAPI
app = FastAPI()

@app.get("/api/check")
async def check_full():
    return {"status": "SUCCESS", "message": "Hit /api/check route"}

@app.get("/")
async def check_root():
    return {"status": "SUCCESS", "message": "Hit function root route"}
