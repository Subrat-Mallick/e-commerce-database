from fastapi import FastAPI
from app.api import customers, products, orders
from app.database.sql import init_db as init_sql_db
from app.database.nosql import init_db as init_nosql_db

app = FastAPI()

app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])


@app.on_event("startup")
async def startup_db():
    # Initialize SQL and NoSQL databases
    init_sql_db()
    init_nosql_db()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
