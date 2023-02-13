import unittest

from mastermind_game import MastermindGame


class TestMastermind(unittest.TestCase):

    """ Test para crear un nuevo juego """
    def test_create_new_game(self):
        # Crea una instancia de la clase Mastermind
        game = MastermindGame()

        # Verifiqua si se ha creado un juego nuevo
        self.assertIsNotNone(game)


    """ Test para comparar una guess con la solución secreta """
    def test_compare_guess(self):
        # Test 1: la suposión es igual a la solución
        game = MastermindGame()
        game.secret_solution = ["R", "R", "B", "B"]
        result = game.compare_guess("RRBB")
        self.assertEqual(result, "BBBB")
        self.assertEqual(game.attempts, 1)

        # Test 2: la suposión tiene dos colores correctos en posiciones correctas y un color correcto pero en posición errónea
        game = MastermindGame()
        game.secret_solution = ["R", "G", "B", "B"]
        result = game.compare_guess("RRGB")
        self.assertEqual(result, "BBW")
        self.assertEqual(game.attempts, 1)

        # Test 1: la suposición no coincide en nada con la solución
        game = MastermindGame()
        game.secret_solution = ["R", "G", "B", "B"]
        result = game.compare_guess("YYYY")
        self.assertEqual(result, "")
        self.assertEqual(game.attempts, 1)


    """ Test para obtener el estado actual del juego """
    def test_get_state(self):
        # Crea una instancia de la clase Mastermind
        game = MastermindGame()

        # Obtiene el estado actual del juego
        state = game.get_state()

        # Verifica si el estado es válido
        self.assertIsNotNone(state)

if __name__ == '__main__':
    unittest.main()