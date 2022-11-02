from fastapi import FastAPI, HTTPException, status
from .router import nilairout , siswarout
app = FastAPI()

app.include_router(nilairout.router)
app.include_router(siswarout.router)
