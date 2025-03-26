from flask import Flask, render_template, jsonify
from game import Game

app = Flask(__name__)

# Spielinstanz erstellen (für jetzt: Einzelspielermodus)
game = Game()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roll")
def roll():
    result = game.roll_dice()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
