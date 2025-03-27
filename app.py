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

#@app.route("/lose", methods=["POST"])
#def lose_hp():
 #   result = game.lose_hp("player")
  #  return jsonify({
   #     "message": "HP reduziert",
    #    "player_hp": game.player_hp,
     #   "status": result  # z. B. "Du hast gewonnen!" oder None
    #})

@app.route("/turn_1", methods=["POST"])
def player_1_turn():
    result = game.player_1_turn()
    return jsonify({
        "message": "Spieler 1 hat gezogen",
        "player_1_hp": game.player_1_hp,
        "player_2_hp": game.player_2_hp,
        "status": result
    })

@app.route("/turn_2", methods=["POST"])
def player_2_turn():
    result = game.player_2_turn()
    return jsonify({
        "message": "Spieler 2 hat gezogen",
        "player_1_hp": game.player_1_hp,
        "player_2_hp": game.player_2_hp,
        "status": result
    })

@app.route("/add", methods=["POST"])
def add_hp():
    result = game.add_hp("player_1", 5)  # oder "player_2", je nach Anwendungsfall
    return jsonify({
        "message": "HP hinzugefügt",
        "player_1_hp": game.player_1_hp,
        "player_2_hp": game.player_2_hp,
        "status": result
    })

@app.route("/restart", methods=["POST"])
def restart():
    global game
    game = Game()  # Erzeugt ein neues Spielobjekt
    return jsonify({"message": "Spiel wurde neu gestartet"})


if __name__ == "__main__":
    app.run(debug=True)
