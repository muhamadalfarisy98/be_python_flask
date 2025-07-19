from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# API provider
API_URL = "http://localhost:8000/products"

@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 10

    response = requests.get(API_URL)
    products = response.json()

    total = len(products)
    start = (page - 1) * per_page
    end = start + per_page
    products_paginated = products[start:end]

    total_pages = (total + per_page - 1) // per_page

    return render_template("index.html",
                           products=products_paginated,
                           page=page,
                           total_pages=total_pages)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "price": float(request.form["price"]),
            "quantity": int(request.form["quantity"]),
        }
        requests.post(API_URL, json=data)
        return redirect(url_for("index"))
    return render_template("create_form.html", title="Create Product")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "price": float(request.form["price"]),
            "quantity": int(request.form["quantity"]),
        }
        requests.put(f"{API_URL}/{id}", json=data)
        return redirect(url_for("index"))
    product = requests.get(f"{API_URL}/{id}").json()
    return render_template("edit_form.html", title="Edit Product", product=product)

@app.route("/delete/<int:id>")
def delete(id):
    requests.delete(f"{API_URL}/{id}")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
