"""
Fetching crime data from the City of Chicago public API.

The API uses “Socrata Query Language” or “SoQL”.
    for more detailed doc go to:
        https://dev.socrata.com/docs/queries/
        there u can find how to use queries and the available functions.

This saved the crimes_df in local memory
"""
from fastapi import FastAPI
import requests
import pandas as pd

BASE_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

def init_crimes_cache(app: FastAPI) -> None:
    """
    When the app starts:
    - Call the Chicago API
    - Cache the DataFrame to crimes_df
    - #TODO: replace with redis db
    - Returns: None
    """
    print("Fetching Chicago crimes data on startup...")
    try:
        resp = requests.get(BASE_URL, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data on startup: {e}")
    data = resp.json()
    crimes_df = pd.DataFrame(data)

    # store on FastAPI state
    app.state.crimes_df = crimes_df

    print(f"Loaded {len(crimes_df)} rows into memory.")
    # print df
    # print(crimes_df)

