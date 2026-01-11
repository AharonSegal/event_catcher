"""
FastAPI router for fetching crime data from the City of Chicago public API.
"""
from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(
    prefix="/chicago",
    tags=["chicago"],
)

BASE_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"


@router.get("/crimes")
def get_crimes(limit: int = 20):
    params = {"$limit": limit}

    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=str(e))

    return resp.json()