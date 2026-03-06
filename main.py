from fastapi import FastAPI

app = FastAPI()

# ── Temporary data — acting as our database for now ──────────
products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
    {'id': 5, 'name': 'Laptop Stand', 'price': 1299, 'category': 'Electronics', 'in_stock': True},
    {'id': 6, 'name': 'Mechanical Keyboard', 'price': 2499, 'category': 'Electronics', 'in_stock': True},
    {'id': 7, 'name': 'Webcam', 'price': 1899, 'category': 'Electronics', 'in_stock': False},
]

# ── Endpoint 0 — Home ────────────────────────────────────────
@app.get('/')
def home():
    return {'message': 'Welcome to our E-commerce API'}

# ── Endpoint 1 — Return all products ──────────────────────────
@app.get('/products')
def get_all_products():
    return {'products': products, 'total': len(products)}

from fastapi import FastAPI

app = FastAPI()

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
]

@app.get("/")
def home():
    return {"message": "Welcome to Products API"}

@app.get("/products")
def get_all_products():
    return {"products": products, "total": len(products)}

from fastapi import FastAPI, Query

app = FastAPI()

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
]

@app.get("/")
def home():
    return {"message": "Welcome to Filter Products API"}

@app.get("/products/filter")
def filter_products(
    category: str = Query(None, description="Electronics or Stationery"),
    max_price: int = Query(None, description="Maximum price"),
    in_stock: bool = Query(None, description="True = in stock only")
):
    result = products
    if category:
        result = [p for p in result if p["category"] == category]
    if max_price:
        result = [p for p in result if p["price"] <= max_price]
    if in_stock is not None:
        result = [p for p in result if p["in_stock"] == in_stock]
    return {"filtered_products": result, "count": len(result)}

from fastapi import FastAPI

app = FastAPI()

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
]

@app.get("/")
def home():
    return {"message": "Welcome to In-stock Products API"}

@app.get("/products/in_stock")
def get_instock_products():
    available = [p for p in products if p["in_stock"]]
    return {"in_stock_products": available, "count": len(available)}

from fastapi import FastAPI

app = FastAPI()

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
]

@app.get("/")
def home():
    return {"message": "Welcome to Products by Category API"}

@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    result = [p for p in products if p["category"].lower() == category_name.lower()]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

from fastapi import FastAPI

app = FastAPI()

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
]

@app.get("/")
def home():
    return {"message": "Welcome to Store Summary API"}

@app.get("/store/summary")
def store_summary():
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories,
    }

from fastapi import FastAPI

app = FastAPI()

# ── Temporary product data ───────────────────────────────────
products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499,  'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook',       'price':  99,  'category': 'Stationery',  'in_stock': True},
    {'id': 3, 'name': 'USB Hub',        'price': 799,  'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set',        'price':  49,  'category': 'Stationery',  'in_stock': True},
    {'id': 5, 'name': 'Laptop Stand',   'price':1299,  'category': 'Electronics', 'in_stock': True},
    {'id': 6, 'name': 'Mechanical Keyboard', 'price':2499, 'category':'Electronics','in_stock': True},
    {'id': 7, 'name': 'Webcam', 'price': 1899, 'category':'Electronics','in_stock': False},
]

# ── Endpoint — Bonus: Best Deal & Premium Pick ───────────────
@app.get("/products/deals")
def get_deals():
    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])
    return {
        "best_deal": cheapest,
        "premium_pick": expensive,
    }

from fastapi import FastAPI

app = FastAPI()

products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
]

@app.get("/")
def home():
    return {"message": "Welcome to Product Search API"}

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    result = [p for p in products if keyword.lower() in p["name"].lower()]
    if not result:
        return {"error": "No products found with this keyword"}
    return {"keyword": keyword, "products": result, "total": len(result)}

