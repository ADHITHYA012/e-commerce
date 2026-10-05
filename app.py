from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Smart Watch", "price": 2000},
    {"id": 3, "name": "Headphones", "price": 1500}
]

@app.route("/")
def home():
    return render_template("index1.html", products=products)

@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]
    cart.append(id)

    session["cart"] = cart

    return redirect("/")

@app.route("/cart")
def cart():

    cart_items = []

    if "cart" in session:
        for item_id in session["cart"]:
            for p in products:
                if p["id"] == item_id:
                    cart_items.append(p)

    return render_template(
        "cart.html",
        cart_items=cart_items
    )

@app.route("/buy/<int:id>")
def buy(id):

    product = None

    for p in products:
        if p["id"] == id:
            product = p

    return render_template(
        "success.html",
        product=product
    )

if __name__ == "__main__":
    app.run(debug=True)
