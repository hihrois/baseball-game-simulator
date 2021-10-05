from game import *

def simulate(setting, batting, batting_stat_normal, batting_stat_on_base, batting_stat_on_long_hit, approach_parameter, result, output):
    for game_counter in range(setting.NUM_OF_GAMES):
        game(setting, game_counter, batting, batting_stat_normal, batting_stat_on_base, batting_stat_on_long_hit, approach_parameter, result, output)