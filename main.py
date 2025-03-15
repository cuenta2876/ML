from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.ai_routes import router as ai_router

app = FastAPI()

app.include_router(user_router)
app.include_router(ai_router)

@app.get("/")
def read_root():
    return {"message": "API de ML funcionando correctamente"}