from fastapi import FastAPI

app = FastAPI(title="AI Model Benchmark API")


@app.get("/")
def root():
    return {"message": "AI Model Benchmark API is running"}