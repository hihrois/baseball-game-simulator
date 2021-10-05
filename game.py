from batting import *
from constant import *
from runner import *

# def game(setting, game_counter, batting, batting_stat, result, output):
def game(setting, game_counter, batting, batting_stat_normal, batting_stat_on_base, batting_stat_on_long_hit, approach_parameter, result, output):
    if setting.IS_INDICATED_BOX_RESULT or setting.IS_INDICATED_GAME_RESULT or (game_counter + 1) % 1000 == 0:
        # print("Game {}: ".format(game_counter + 1))
        pass

    #初期化
    inning, outcount, runner, batting_order = [1, 0, 0, 1]
    run_list = [0] * setting.INNING
    or_memo = []
    or_memo_order = []

    while inning <= setting.INNING:
		#得点期待値表制作用、[アウトカウント、ランナー、その時点でのイニング得点数、最後の０はイニング終了時の得点]
        or_memo.append([outcount, runner207(runner), run_list[inning - 1], 0])
		#打順別得点期待値表制作用、[打順要素を追加]
        or_memo_order.append([batting_order, outcount, runner207(runner), run_list[inning - 1], 0])
        #関数『打者』と関数『走塁』を呼び出す
        # simulate_batting_result(batting_order, batting_stat_normal, batting_stat_on_base, batting_stat_on_long_hit, approach_parameter, outcount, runner):
        event = batting.simulate_batting_result(batting_order, batting_stat_normal, batting_stat_on_base, batting_stat_on_long_hit, approach_parameter, outcount, runner207(runner))
        if setting.IS_INDICATED_BOX_RESULT:
            print("BoxScore Result {}".format(event))
		
		#LWTS
        before_outcount, before_runner = [outcount, runner207(runner)]
		#イベント前の得点期待値
        before_RE = RE[before_outcount][before_runner]
		#Nを数える
        # LWTS_N[event206(event)] += 1
        outcount, runner, run, change_flg = run_move(outcount, runner, event, batting_order, TRS, N)
		#LWTS
        after_RE = run if change_flg else run + RE[outcount][runner207(runner)]

		#イベント前後の得点期待値変動
        # LWTS[event206(event)] += after_RE - before_RE


        # print(outcount, runner, run)
		
        batting_order += 1 #打順を1つ進める
        if batting_order == 10:
            batting_order = 1
        
        run_list[inning - 1] += run #イニング得点を記録
		
        if change_flg:
			#or_memoの最後にイニング終了時得点を記録
            for i in range(len(or_memo)):
                or_memo[i][3] = run_list[inning - 1]
            for i in range(len(or_memo_order)):
                or_memo_order[i][4] = run_list[inning - 1]
			#得点期待値表への書き込み
            output.write_re_tmp(or_memo)
            output.write_re_order_tmp(or_memo_order)
			#初期化
            or_memo = []
            or_memo_order = []
			#次のイニングへ行く処理
            inning += 1

	#9イニングでの得点を記録
    run_total = int(sum(run_list))

    _result = result.game_results[game_counter]
    _result.run = run_total

    if setting.IS_INDICATED_GAME_RESULT:
        print("Run {}".format(run_total))
    
    return 0