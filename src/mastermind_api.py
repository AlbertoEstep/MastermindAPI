from flask import Flask, jsonify, request
from mastermind_game import MastermindGame

app = Flask(__name__)
games = {}

@app.route('/', methods=['GET'])
def ping():
    return {"response": "Mastermind"}

@app.route('/mastermind/new_game', methods=['POST'])
def new_game():
    # Creo una nueva instancia del juego Mastermind
    game = MastermindGame()
    # Guardo la instancia del juego en un diccionario para poder acceder a ella más tarde
    game_id = len(games)
    games[game_id] = game
    # Devuelvo el ID del juego creado
    return {"game_id": game_id}

@app.route('/mastermind/status/<int:game_id>', methods=['GET'])
def get_game(game_id):
    # Obtengo el estado actual del juego
    state = games[game_id].get_state()
    # Devuelvo el estado actual del juego en formato JSON
    return jsonify(state)

@app.route('/mastermind/guess/<int:game_id>', methods=['POST'])
def make_guess(game_id):
    # Obtengo la guess de la solicitud
    guess = request.json["guess"]
    # Comparo la guess con la solución secreta y obtengo el resultado
    result = games[game_id].compare_guess(guess)
    # Devuelvo el resultado
    return jsonify({"result": result})

@app.route("/mastermind/check_guess/<int:game_id>", methods=["POST"])
def check_guess(game_id):
    # Obtengo la guess del request
    guess = request.json.get("guess")
    # Verifico que la guess sea una cadena de 4 letras
    if type(guess) != str or len(guess) != 4:
        return jsonify({"error": "La guess debe ser una cadena de 4 letras"}), 400
    # Verifico que todas las letras de la guess estén dentro de los colores permitidos
    for letter in guess:
        if letter not in games[game_id].colors:
            return jsonify({"error": f"{letter} no es un color permitido"}), 400
    # Si todas las verificaciones son correctas, devuelvo un código 200
    return jsonify({"message": "Guess válida"}), 200

@app.route("/mastermind/check_game/<int:game_id>", methods=["GET"])
def check_game(game_id):
    # Verifico que el juego existe
    if game_id not in games:
        return jsonify({"error": "El juego ya no existe"}), 400
    # Si todas las verificaciones son correctas, devuelvo un código 200
    return jsonify({"message": "Juego válido"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)