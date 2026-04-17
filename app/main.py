from fastapi import FastAPI
from app.api.routes_email import router as email_router

app = FastAPI(title="AI Email Assistant SaaS")

app.include_router(email_router)