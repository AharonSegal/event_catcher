# app/main.py

from fastapi import FastAPI, HTTPException
import os
import json
import requests
import pandas as pd
import redis

BASE_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

# Redis connection config (service name in compose = "redis")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,  # get strings instead of bytes
)

app = FastAPI()


@app.lifespan("startup")
def fetch_and_cache_crimes_on_startup():
    """
    When the app starts:
    - Call the Chicago API
    - Save the raw JSON into Redis
    """
    print("Fetching Chicago crimes data on startup...")


    try:
        resp = requests.get(BASE_URL, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data on startup: {e}")
        return  

    data = resp.json()

    # Save raw JSON string to Redis
    redis_client.set("chicago:crimes", json.dumps(data))
    print("Initial crimes data cached in Redis under key 'chicago:crimes'")


@app.get("/crimes")
def get_crimes(limit: int | None = None):
    """
    Return crimes data from Redis cache.
    - If limit is given, slice the list.
    """
    cached = redis_client.get("chicago:crimes")
    if cached is None:
        raise HTTPException(status_code=503, detail="Data not loaded yet")

    all_data = json.loads(cached)

    if limit is not None:
        return all_data[:limit]

    return all_data


@app.get("/crimes/df-info")
def crimes_df_info():
    """
    Example endpoint to show DataFrame info rebuilt from Redis JSON.
    """
    cached = redis_client.get("chicago:crimes")
    if cached is None:
        raise HTTPException(status_code=503, detail="Data not loaded yet")

    data = json.loads(cached)
    df = pd.DataFrame(data)

    return {
        "rows": int(df.shape[0]),
        "columns": list(df.columns),
    }