from flask import Flask, request, jsonify, render_template
import difflib
from faq_data import faq

app = Flask(__name__)

def get_answer(user_input):
    user_input = user_input.lower()

    # Keyword-based checks first
    if "menu" in user_input or "cakes" in user_input:
        formatted_menu = (
            "🍰 **Menu:**\n"
            "Birthday Cake - PKR 3,200\n"
            "Wedding Cake - PKR 3,000\n"
            "Chocolate Cake - PKR 1,500\n"
            "Vanilla Cake - PKR 1,400\n"
            "Red Velvet - PKR 1,600\n"
            "Black Forest - PKR 1,700\n"
            "Strawberry Cake - PKR 1,500\n"
            "Carrot Cake - PKR 1,400\n"
            "🧁 Cupcake Set of 6 - PKR 1,800\n\n"
            "🎉 **Combos:**\nBirthday Combo, Party Combo, Special Offer Combo"
        )
        return formatted_menu

    # Fuzzy match with FAQ
    match = difflib.get_close_matches(user_input, faq.keys(), n=1, cutoff=0.5)
    if match:
        return faq[match[0]]
    else:
        return "Sorry, I didn’t understand. Please ask about cakes, orders, or delivery."


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = get_answer(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
