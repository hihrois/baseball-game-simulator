from numpy import *

#runnerを0~7の数字に変換する関数
def runner207(runner):
    num_list = [0, 1, 2, 12, 3, 13, 23, 123]
    return num_list.index(runner)

#eventを0~6の数字に変換する関数
def event206(event):
    event_list = ["single", "double", "triple", "hr", "bb", "so", "bonda"]
    return event_list.index(event)

#ランナーの数を数える関数(1 -> 1, 12 -> 2, 0 -> 0)i
def count_run(runner):
    if runner == 0: return 0
    else: return len(str(runner))
			
#「チェンジになったけど得点は入った」を処理する関数（好ましくない、将来的に改善が必要）	
def run_and_change_cal(runner, event):
	run = 0
	#参照表(runner, event, その時に出力する得点)
	#1, 2, 12, 3, 13, 23, 123
	ore_run = [
        [3,   "single", 1], 
        [13,  "single", 1], 
        [23,  "single", 1], 
        [123, "single", 1], 
        [2,   "double", 1], 
        [12,  "double", 1], 
        [3,   "double", 1], 
        [13,  "double", 1], 
        [23,  "double", 2], 
        [123, "double", 2]
    ]
	if event in ["bonda", "so", "bb"]: return run
	elif event == "triple": return count_run(runner)
	else:
		for i in range(10):
			if event == ore_run[i][1] and runner == ore_run[i][0]:
				run = ore_run[i][2]
				break
		return run

#関数『走者』	
def run_move(outcount, runner, event, order, TRS, N):
    length = len(TRS[outcount][runner207(runner)][event206(event)])
    #遷移する（アウト）のリスト
    trs_outcount_list = [TRS[outcount][runner207(runner)][event206(event)][i][0] for i in range(length)]
    #遷移する（ランナー）のリスト
    trs_runner_list = [TRS[outcount][runner207(runner)][event206(event)][i][1] for i in range(length)]
    #遷移する確率のリスト
    trs_p_list = [TRS[outcount][runner207(runner)][event206(event)][i][2] / N[outcount][runner207(runner)][event206(event)] for i in range(length)]

    #random.choiceが選択するためのリスト
    trs_choose_list = [i for i in range(length)]
    #ランダムに選択
    trs_rst = random.choice(trs_choose_list, p = trs_p_list)
    #print("%dアウト　%d塁" %(trs_outcount_list[trs_rst], trs_runner_list[trs_rst]))
    next_outcount = trs_outcount_list[trs_rst]
    if next_outcount == 3:
        next_outcount = 0
        
    next_runner = trs_runner_list[trs_rst]

    #得点計算(アウトカウントとランナーの数+1から、次のアウトカウントと次のランナーを引いた数が得点になる)
	#チェンジ判定
    change_flg = 0
    if outcount > next_outcount:
        run = run_and_change_cal(runner, event)
        # global left
		# left += count_run(runner) - run
        change_flg = 1
    else:
        run = outcount + count_run(runner) + 1 - next_outcount - count_run(next_runner)

    return [next_outcount, next_runner, run, change_flg]