# app/main.py
from fastapi import FastAPI
from app.orders import routers as order_routers
from app.products import routers as product_routers
from app.users import routers as user_routers

app = FastAPI()

# Include routers for each app module
app.include_router(order_routers.router, prefix="/orders", tags=["orders"])
app.include_router(product_routers.router, prefix="/products", tags=["products"])
app.include_router(user_routers.router, prefix="/users", tags=["users"])
