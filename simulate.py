from game import *

def simulate(setting, result):
    for game_counter in range(setting.NUM_OF_GAMES):
        game(setting, game_counter, result)