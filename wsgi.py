from backend.main import app  # 👈 now correctly imports your FastAPI app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
