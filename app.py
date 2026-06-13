from flask import Flask, render_template, redirect

app = Flask(__name__)

coffee_items = [
    {"id": 1, "name": "Cappuccino", "votes": 0},
    {"id": 2, "name": "Latte", "votes": 0},
    {"id": 3, "name": "Espresso", "votes": 0}
]

@app.route("/")
def home():
    return render_template("index.html", items=coffee_items)

@app.route("/vote/<int:item_id>")
def vote(item_id):
    for item in coffee_items:
        if item["id"] == item_id:
            item["votes"] += 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)