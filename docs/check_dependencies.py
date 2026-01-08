"""
check_dependencies.py
---------------------
This script tests whether the key Python libraries (grouped by category)
required for this project are installed and functional.

Usage:
------
1. Activate your virtual environment:
    source venv/Scripts/activate
2. Run:
    python check_dependencies.py
"""

import traceback
import os

# --------------------------
# Toggle which tests to run (grouped by category)
# --------------------------
TEST_LIBRARIES = {
    "Standard Library": {
        # Built-in, no need to install, just verify import
        "os": True,
        "sys": True,
        "json": True,
        "datetime": True,
        "pathlib": True,
        "logging": True,
    },
    "Databases": {
        "sqlite3": True,
        "SQLAlchemy": True,
        "SQLModel": True,
    },
    "Web & APIs": {
        "FastAPI": True,
        "Requests": True,
        "Uvicorn": True,
    },
    "Pydantic & Validation": {
        "Pydantic": True,
    },
    "Environment & Configuration": {
        "python-dotenv": True,
        "configparser": True,
    },
    "Data Analysis & Visualization": {
        "NumPy": True,
        "Pandas": True,
        "Matplotlib": True,
        "Seaborn": True,
    },
    "Utilities": {
        # Optional utility checks
        "functools": True,
        "itertools": True,
        "random": True,
    }
}

# --------------------------
# Store results + errors
# --------------------------
results = {}
errors = {}

# --------------------------
# Generic import tester
# --------------------------
def test_import(name, func):
    print(f"\n=== Testing {name} ===")
    try:
        func()
        print(f"[PASS] {name} works")
        results[name] = True
    except Exception as e:
        print(f"[FAIL] {name} error:")
        print(type(e).__name__, e)
        traceback.print_exc()
        results[name] = False
        errors[name] = f"{type(e).__name__}: {e}"

# --------------------------
# Test functions by library
# --------------------------
def test_sqlalchemy():
    import sqlalchemy
    from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
    engine = create_engine("sqlite:///:memory:")
    metadata = MetaData()
    Table("items", metadata, Column("id", Integer, primary_key=True), Column("name", String))
    metadata.create_all(engine)

def test_sqlmodel():
    from sqlmodel import SQLModel, Field, create_engine, Session
    class Item(SQLModel, table=True):
        id: int | None = Field(default=None, primary_key=True)
        name: str
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(Item(name="example"))
        session.commit()

def test_fastapi():
    from fastapi import FastAPI
    app = FastAPI()
    assert callable(app.get)

def test_pydantic():
    from pydantic import BaseModel, EmailStr
    class User(BaseModel):
        email: EmailStr
    User(email="test@example.com")

def test_requests():
    import requests
    response = requests.Response()
    assert isinstance(response, requests.Response)

def test_uvicorn():
    import uvicorn
    assert hasattr(uvicorn, "run")

def test_dotenv():
    from dotenv import load_dotenv
    open(".env", "w").write("TEST_VALUE=123")
    load_dotenv()
    assert os.getenv("TEST_VALUE") == "123"

def test_configparser():
    import configparser
    config = configparser.ConfigParser()
    config.read_dict({"section": {"key": "value"}})
    assert config["section"]["key"] == "value"

def test_numpy():
    import numpy as np
    arr = np.array([1, 2, 3])
    assert arr.sum() == 6

def test_pandas():
    import pandas as pd
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    assert df["a"].sum() == 3
    assert df["b"].sum() == 7

def test_matplotlib():
    import matplotlib.pyplot as plt
    assert hasattr(plt, 'figure')
    assert callable(plt.figure)

def test_seaborn():
    import seaborn as sns
    import pandas as pd
    df = pd.DataFrame({"x": [1,2,3], "y": [3,2,1]})
    plot = sns.scatterplot(data=df, x="x", y="y")
    assert plot is not None

# --------------------------
# Map library names to test functions
# --------------------------
TEST_FUNCTIONS = {
    "SQLAlchemy": test_sqlalchemy,
    "SQLModel": test_sqlmodel,
    "FastAPI": test_fastapi,
    "Pydantic": test_pydantic,
    "Requests": test_requests,
    "Uvicorn": test_uvicorn,
    "python-dotenv": test_dotenv,
    "configparser": test_configparser,
    "NumPy": test_numpy,
    "Pandas": test_pandas,
    "Matplotlib": test_matplotlib,
    "Seaborn": test_seaborn,
}

# --------------------------
# Run tests
# --------------------------
if __name__ == "__main__":
    print("\n### PYTHON DEPENDENCY DIAGNOSTICS ###")
    
    for category, libs in TEST_LIBRARIES.items():
        print(f"\n--- Category: {category} ---")
        for name, enabled in libs.items():
            if enabled and name in TEST_FUNCTIONS:
                test_import(name, TEST_FUNCTIONS[name])
            elif enabled:
                try:
                    __import__(name)
                    print(f"[PASS] {name} works")
                    results[name] = True
                except Exception as e:
                    print(f"[FAIL] {name} error:")
                    print(type(e).__name__, e)
                    results[name] = False
                    errors[name] = f"{type(e).__name__}: {e}"
            else:
                print(f"[SKIPPED] {name}")
                results[name] = None

    # --------------------------
    # Final Detailed Summary
    # --------------------------
    print("\n### FINAL DETAILED SUMMARY ###")
    for name, status in results.items():
        state = "PASS" if status is True else "FAIL" if status is False else "SKIPPED"
        print(f"- {name}: {state}")

    passed = sum(1 for x in results.values() if x)
    total = sum(1 for x in results.values() if x is not None)
    print(f"\nOverall: {passed}/{total} tests passed")

    if errors:
        print("\n### SHORT ERROR SUMMARY ###")
        for name, err in errors.items():
            print(f"- {name}: {err}")
    else:
        print("\nNo errors. All good.")
