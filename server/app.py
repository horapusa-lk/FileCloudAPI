from fastapi import FastAPI

from server.routes.fileRoute import router

app = FastAPI()

app.include_router(router, tags=["Cloud"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}