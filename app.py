from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "food-ordering-demo-secret"

MENU = [
    {"id": 1, "name": "Margherita Pizza", "category": "Pizza", "price": 299, "emoji": "🍕"},
    {"id": 2, "name": "Veg Burger", "category": "Burger", "price": 149, "emoji": "🍔"},
    {"id": 3, "name": "Paneer Tikka", "category": "Starters", "price": 229, "emoji": "🍢"},
    {"id": 4, "name": "Masala Dosa", "category": "Indian", "price": 129, "emoji": "🥞"},
    {"id": 5, "name": "Chicken Biryani", "category": "Biryani", "price": 249, "emoji": "🍛"},
    {"id": 6, "name": "French Fries", "category": "Sides", "price": 99, "emoji": "🍟"},
    {"id": 7, "name": "Cold Coffee", "category": "Drinks", "price": 119, "emoji": "🥤"},
    {"id": 8, "name": "Chocolate Brownie", "category": "Dessert", "price": 139, "emoji": "🍫"},
]

@app.route("/")
def index():
    return render_template("index.html", menu=MENU, cart=session.get("cart", {}))

@app.post("/add/<int:item_id>")
def add_to_cart(item_id):
    cart = session.get("cart", {})
    key = str(item_id)
    cart[key] = cart.get(key, 0) + 1
    session["cart"] = cart
    return redirect(url_for("index") + "#menu")

@app.post("/remove/<int:item_id>")
def remove_from_cart(item_id):
    cart = session.get("cart", {})
    key = str(item_id)
    if key in cart:
        cart[key] -= 1
        if cart[key] <= 0:
            del cart[key]
    session["cart"] = cart
    return redirect(url_for("index") + "#cart")

@app.post("/checkout")
def checkout():
    session.pop("cart", None)
    return render_template("index.html", menu=MENU, cart={}, message="Order placed successfully! 🍽️")

@app.get("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
