from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(**name**)
app.secret_key = os.environ.get("SECRET_KEY", "shopeasy-demo-key-2026")

products = [
{"id": 1, "name": "Laptop", "price": 55000, "image": "images/laptop.jpg", "category": "Electronics"},
{"id": 2, "name": "Smart Watch", "price": 2000, "image": "images/watch.jpg", "category": "Accessories"},
{"id": 3, "name": "Headphones", "price": 1500, "image": "images/headphone.jpg", "category": "Electronics"},
{"id": 4, "name": "Bluetooth Speaker", "price": 2500, "image": "images/speaker.jpg", "category": "Electronics"},
{"id": 5, "name": "Mobile Phone", "price": 25000, "image": "images/mobile.jpg", "category": "Mobiles"},
{"id": 6, "name": "Gaming Mouse", "price": 1200, "image": "images/mouse.jpg", "category": "Accessories"},
{"id": 7, "name": "Keyboard", "price": 999, "image": "images/keyboard.jpg", "category": "Accessories"}
]

@app.route("/")
def home():
search = request.args.get("search", "").strip()
category = request.args.get("category", "").strip()

```
filtered_products = products.copy()

if search:
    filtered_products = [
        p for p in filtered_products
        if search.lower() in p["name"].lower()
        or search.lower() in p["category"].lower()
    ]

if category:
    filtered_products = [
        p for p in filtered_products
        if p["category"].lower() == category.lower()
    ]

cart = session.get("cart", {})
cart_count = sum(cart.values())
categories = sorted(set(p["category"] for p in products))

return render_template(
    "index1.html",
    products=filtered_products,
    search=search,
    category=category,
    categories=categories,
    cart_count=cart_count
)
```

@app.route("/add_to_cart/[int:product_id](int:product_id)", methods=["POST"])
def add_to_cart(product_id):
product = next((p for p in products if p["id"] == product_id), None)

```
if product is None:
    return "Product not found", 404

cart = session.get("cart", {})
key = str(product_id)
cart[key] = cart.get(key, 0) + 1

session["cart"] = cart
session.modified = True

return redirect(url_for("cart"))
```

@app.route("/cart")
def cart():
cart_data = session.get("cart", {})
cart_items = []
total = 0

```
for product in products:
    quantity = cart_data.get(str(product["id"]), 0)

    if quantity > 0:
        item = product.copy()
        item["quantity"] = quantity
        item["subtotal"] = product["price"] * quantity
        cart_items.append(item)
        total += item["subtotal"]

cart_count = sum(cart_data.values())

return render_template(
    "cart.html",
    cart_items=cart_items,
    total=total,
    cart_count=cart_count
)
```

@app.route("/remove_from_cart/[int:product_id](int:product_id)", methods=["POST"])
def remove_from_cart(product_id):
cart_data = session.get("cart", {})
cart_data.pop(str(product_id), None)

```
session["cart"] = cart_data
session.modified = True

return redirect(url_for("cart"))
```

@app.route("/buy/[int:product_id](int:product_id)", methods=["POST"])
def buy(product_id):
product = next((p for p in products if p["id"] == product_id), None)

```
if product is None:
    return "Product not found", 404

return render_template(
    "success.html",
    product=product,
    quantity=1,
    total=product["price"]
)
```

@app.route("/checkout", methods=["POST"])
def checkout():
cart_data = session.get("cart", {})

```
if not cart_data:
    return redirect(url_for("cart"))

cart_items = []
total = 0

for product in products:
    quantity = cart_data.get(str(product["id"]), 0)

    if quantity > 0:
        item = product.copy()
        item["quantity"] = quantity
        item["subtotal"] = product["price"] * quantity
        cart_items.append(item)
        total += item["subtotal"]

session["cart"] = {}
session.modified = True

return render_template(
    "order_success.html",
    cart_items=cart_items,
    total=total
)
```

if **name** == "**main**":
app.run(debug=True)
