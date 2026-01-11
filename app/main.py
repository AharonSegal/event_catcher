from fastapi import FastAPI
from app.api.api_data import init_crimes_cache
from app.api.queries import router as queries_router  # <-- new


print("11111111111111111111")

app = FastAPI()

# load and attach DataFrame before "2222..."
init_crimes_cache(app)
# queries endpoints
app.include_router(queries_router)

print("2222222222222222222")