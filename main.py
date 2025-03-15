import os
os.system("pip install --no-cache-dir torch transformers")
import uvicorn
from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.ai_routes import router as ai_router

app = FastAPI()

app.include_router(user_router)
app.include_router(ai_router)

@app.get("/")
def read_root():
    return {"message": "API de ML funcionando correctamente"}

# Esto asegura que Render use el puerto correcto
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Usa el puerto de Render o 8000 por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)