
from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route('/')
def hello_world():
    test = "test text"

    cards = [1,2,3]

    # tarot_reading_cards = main.main()
    # for card in tarot_reading_cards:
    #     cards.append(card[2])

    return render_template("index.html", test=test, card_images=cards)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
