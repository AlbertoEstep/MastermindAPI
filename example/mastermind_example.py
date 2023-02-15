import requests
import time
import keyboard


def print_state(url, game_id):
    response = requests.get(f"{url}mastermind/status/{game_id}")
    game_status = response.json()
    # Printeo
    print('\n\n')
    print("-------------------------------")
    print("  Turno  | Intento | Resultado")
    print("-------------------------------")
    for attempt in game_status['history_attempts']:
        print("{:8} |   {}  |  {}".format(attempt, game_status['history_attempts'][attempt][0], game_status['history_attempts'][attempt][1]))
        
def win(url, game_id):
    response = requests.get(f"{url}mastermind/status/{game_id}")
    game_status = response.json()
    if game_status['win']:
        return True
    else:
        return False

def lose(url, game_id):
    response = requests.get(f"{url}mastermind/status/{game_id}")
    game_status = response.json()
    if game_status['lose']:
        return True
    else:
        return False

def print_win():
    while True:
        print("\rYOU'RE WINNING!!", end="")
        time.sleep(0.5)
        print("\r                ", end="")
        time.sleep(0.5)
        if keyboard.is_pressed('q'):
            break

def print_lose():
    while True:
        print("\rYou lost the game...", end="")
        time.sleep(0.5)
        print("\r                    ", end="")
        time.sleep(0.5)
        if keyboard.is_pressed('q'):
            break


if __name__ == '__main__':
    # Dirección URL del servidor que ejecuta la API
    url = "http://localhost:4000/"

    # Creación de un nuevo juego
    response = requests.post(f"{url}mastermind/new_game")

    if response.status_code == 200:
        response_json = response.json()
        # Obtención del estado actual del juego
        response = requests.get(f"{url}mastermind/status/{response_json['game_id']}")
        game_status = response.json()

        print(game_status)
        # Desarrollo del juego por consola
        is_game = True
        while is_game:
            response_check_game = requests.get(f"{url}mastermind/check_game/{response_json['game_id']}")
            check_game_result = response.json()
            if response_check_game.status_code == 200:
                print_state(url, response_json['game_id'])
                guess = input('Introduce una nueva suposición: ')
                response_check_guess = requests.post(f"{url}mastermind/check_guess/{response_json['game_id']}", json={"guess": guess})
                if response_check_guess.status_code == 200:
                    check_guess_result = response_check_guess.json()
                    response = requests.post(f"{url}mastermind/guess/{response_json['game_id']}", json={"guess": guess})
                    guess_result = response.json()
                else:
                    check_guess_result = response_check_guess.json()
                    print(check_guess_result['error'])
            else:
                check_game_result = response_check_guess.json()
                print(check_game_result['error'])
            if win(url, response_json['game_id']):
                print_win()
                break
            elif lose(url, response_json['game_id']):
                print_lose()
                break
    else:
        print('Error: No se ha podido crear el juego')