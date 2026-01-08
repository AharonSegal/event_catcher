from fastapi import APIRouter
from datetime import datetime, timezone
from models import Event

router = APIRouter(
    prefix="/events",
    tags=["events"],
)

