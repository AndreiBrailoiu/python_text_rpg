import pickle

class SaveLoad:
    @staticmethod
    def save_game(game_state, filename):
        with open(filename, 'wb') as file:
            pickle.dump(game_state, file)

    @staticmethod
    def load_game(filename):
        try:
            with open(filename, 'rb') as file:
                game_state = pickle.load(file)
            return game_state
        except FileNotFoundError:
            return None