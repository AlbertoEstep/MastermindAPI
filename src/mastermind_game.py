import random

class MastermindGame:
    """
        Este método se ejecutará al crear una nueva instancia de la clase y se encargará de generar una solución secreta.
    """
    def __init__(self):
        # Inicializo los posibles colores
        self.colors = ["R", "G", "B", "Y", "O", "P"]
        # Creo una solución para el juego inicializado
        self.secret_solution = [random.choice(self.colors) for i in range(4)]
        # Inicializo la variable turnos
        self.attempts = 0
        self.history_attempts = {}
        self.win = False
        self.lose = False

    def set_history_attemps(self, guess, result):
        self.history_attempts.update({self.attempts: (guess, result)})
    
    """
        Este método recibirá una guess y comparará con la solución secreta. Devolverá una respuesta en forma de string con la cantidad de fichas que están en el lugar correcto y cuántas están en el juego pero en la posición incorrecta.
    """
    def compare_guess(self, guess):
        result = ""
        list_guess = list(guess)
        secret_solution = self.secret_solution.copy()
        # Busco aquellas chinchetas con misma posición y mismo color y añado al resultado devuelto una chincheta negra por cada coincidencia
        for i in range(4):
            if list_guess[i] == secret_solution[i]:
                result += "B"
                list_guess[i] = "X"
                secret_solution[i] = "X"
        # Busco aquellas chinchetas con mismo color y distinta posición y añado al resultado devuelto una chincheta blanca por cada coincidencia
        for i in range(4):
            if list_guess[i] in secret_solution and list_guess[i] != "X":
                result += "W"
                index = secret_solution.index(list_guess[i])
                secret_solution[index] = "X"
        # Sumo un turno y actualizo el histórico de intentos
        self.attempts += 1
        self.set_history_attemps(guess, result)
        if result == 'BBBB':
            self.win = True
        elif self.attempts > 10:
            self.lose = True
        # Devuelvo el resultado
        return result
    
    """
         Este método devolverá el estado actual del juego, incluyendo la solución secreta y la cantidad de intentos realizados hasta el momento.
    """
    def get_state(self):
        return {"secret_solution": "".join(self.secret_solution), "attempts": self.attempts, 'history_attempts': self.history_attempts, 'win': self.win, 'lose': self.lose}
