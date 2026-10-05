from flask import Flask, render_template, request

app1 = Flask(__name__)

products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Smart Watch", "price": 2000},
    {"name": "Headphones", "price": 1500},
    {"name": "Bluetooth Speaker", "price": 2500},
    {"name": "Mobile Phone", "price": 25000}
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
        "index.html",
        products=filtered_products,
        search=search
    )

if __name__ == "__main__":
    app.run(debug=True)
