from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("store.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = get_db()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()

    search = request.args.get("search", "")

    if search:
        products = [p for p in products if search.lower() in p["name"].lower()]

    return render_template("index1.html", products=products, search=search)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]

        conn = get_db()
        conn.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            (name, price)
        )
        conn.commit()
        conn.close()

        return redirect("/admin")

    conn = get_db()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()

    return render_template("admin.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
