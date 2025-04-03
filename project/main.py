from routes import router
from models import Base
from dependencies import engine
from fastapi import FastAPI
from config import CACHE_TTL
from datetime import timedelta

app = FastAPI()

# Creating database tables
Base.metadata.create_all(bind=engine)

# Including routes
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    """Setting cache lifetime on startup"""
    app.state.cache_ttl = timedelta(minutes=CACHE_TTL)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)