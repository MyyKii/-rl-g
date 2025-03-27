from flask import Flask, render_template, jsonify
from game import Game

app = Flask(__name__)

# Spielinstanz erstellen (für jetzt: Einzelspielermodus)
game = Game()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/status")
def status():
    return jsonify(game.get_status())

@app.route("/roll")
def roll():
    result = game.roll_dice()
    return jsonify(result)

@app.route("/lose", methods=["POST"])
def lose_hp():
    result = game.lose_hp("player")
    return jsonify({
        "message": "HP reduziert",
        "player_hp": game.player_hp,
        "status": result  # z. B. "Du hast gewonnen!" oder None
    })

@app.route("/add", methods=["POST"])
def add_hp(): 
    result = game.add_hp("player", 5)
    return jsonify({
        "message": "HP hinzugefügt",
        "player_hp": game.player_hp,
        "status": result  # z. B. "Du hast gewonnen!" oder None
    })

@app.route("/restart", methods=["POST"])
def restart():
    global game
    game = Game()  # Erzeugt ein neues Spielobjekt
    return jsonify({"message": "Spiel wurde neu gestartet"})


if __name__ == "__main__":
    app.run(debug=True)
