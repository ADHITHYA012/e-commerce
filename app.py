from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Smart Watch", "price": 2000},
    {"name": "Headphones", "price": 1500},
    {"name": "Bluetooth Speaker", "price": 2500},
    {"name": "Mobile Phone", "price": 25000},
    {"name": "Gaming Mouse", "price": 1200}
]

@app.route("/")
def home():

    search = request.args.get("search", "")

    if search:
        filtered_products = [
            p for p in products
            if search.lower() in p["name"].lower()
        ]
    else:
        filtered_products = products

    return render_template(
        "index1.html",
        products=filtered_products,
        search=search
    )

@app.route("/success")
def success():
    return """
    <h1>✅ Order Placed Successfully!</h1>
    <br>
    <a href="/">Back To Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
