from setting import *
from batting import *

def simulate_game():
    batting_order = 1
    for inning in range(INNING):
        # カウンターの初期化
        outcount = 0
        runner = [0] * 3

        while outcount != 3:
            print(simulate_batting_result(batting_order, outcount, runner))
            break