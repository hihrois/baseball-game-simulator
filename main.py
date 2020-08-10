from game import *
from setting import *
from batting import *

# 打撃成績の読み込み
read_batting_stats(FILE_NAME)

# シミュレート
for game_counter in range(NUM_OF_GAMES):
    simulate_game()