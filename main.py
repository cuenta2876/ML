import os
os.system("pip install --no-cache-dir torch transformers")
import uvicorn
from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.ai_routes import router as ai_router



[2025-03-15 23:10:08 +0000] [1] [ERROR] Worker (pid:7) exited with code 3
[2025-03-15 23:10:08 +0000] [1] [ERROR] Shutting down: Master
[2025-03-15 23:10:08 +0000] [1] [ERROR] Reason: Worker failed to boot.


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