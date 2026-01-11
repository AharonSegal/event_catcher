from fastapi import APIRouter, Request, HTTPException, Query
from typing import Optional

router = APIRouter(
    prefix="/crimes",
    tags=["crimes"],
)

@router.get("/head")
async def crimes_head(
    request: Request,
    limit: int = Query(10, ge=1, le=1000),
):
    """
    Return the first `limit` rows from crimes_df
    """
    # Get the DataFrame from FastAPI state
    df = getattr(request.app.state, "crimes_df", None)

    if df is None:
        raise HTTPException(status_code=500, detail="crimes_df not loaded in app.state")

    subset = df.head(limit)
    # Convert pandas DataFrame to JSON-serializable format
    return subset.to_dict(orient="records")


@router.get("/by-primary-type")
async def crimes_by_primary_type(
    request: Request,
    primary_type: str,
    limit: int = Query(100, ge=1, le=5000),
):
    """
    Example filter with a pandas query:
    /crimes/by-primary-type?primary_type=THEFT
    """
    df = getattr(request.app.state, "crimes_df", None)

    if df is None:
        raise HTTPException(status_code=500, detail="crimes_df not loaded in app.state")

    # Pandas filter
    filtered = df[df["primary_type"] == primary_type.upper()].head(limit)

    return filtered.to_dict(orient="records")


@router.get("/between-dates")
async def crimes_between_dates(
    request: Request,
    start: str,
    end: str,
    limit: int = Query(100, ge=1, le=5000),
):
    """
    Example date-range query using pandas.
    Assumes `date` column exists in crimes_df.
    Dates as ISO strings: 2026-01-01T00:00:00.000
    """
    df = getattr(request.app.state, "crimes_df", None)

    if df is None:
        raise HTTPException(status_code=500, detail="crimes_df not loaded in app.state")

    # ensure date column is datetime
    if df["date"].dtype == "object":
        df = df.copy()
        df["date"] = pd.to_datetime(df["date"])
        # optionally re-store this back into state, so conversion happens once
        request.app.state.crimes_df = df

    start_ts = pd.to_datetime(start)
    end_ts = pd.to_datetime(end)

    mask = (df["date"] >= start_ts) & (df["date"] <= end_ts)
    filtered = df.loc[mask].head(limit)

    return filtered.to_dict(orient="records")