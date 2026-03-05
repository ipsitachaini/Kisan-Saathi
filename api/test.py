from fastapi import FastAPI
app = FastAPI()

@app.get("/api/test")
def test():
    return {"message": "API Test Successful. FastAPI is running."}
