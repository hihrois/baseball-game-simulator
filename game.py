#ランナーの数を数える関数(1 -> 1, 12 -> 2, 0 -> 0)
def count_run(runner):
	if runner == 0:
		return 0
	else:
		return len(str(runner))
		
#runnerを0~7の数字に変換する関数
def runner207(runner):
	for i in range(8):
		num_list = [0, 1, 2, 12, 3, 13, 23, 123]
		if runner == num_list[i]:
			break
	return i
	
#eventを0~6の数字に変換する関数
def event206(event):
	for i in range(7):
		event_list = ["single", "double", "triple", "hr", "bb", "so", "bonda"]
		if event == event_list[i]:
			break
	return i
			
#「チェンジになったけど得点は入った」を処理する関数（好ましくない、将来的に改善が必要）	
def run_and_change_cal(runner, event):
	run = 0
	#参照表(runner, event, その時に出力する得点)
	#1, 2, 12, 3, 13, 23, 123
	ore_run = [[3, "single", 1], [13, "single", 1], [23, "single", 1], [123, "single", 1], [2, "double", 1], [12, "double", 1], [3, "double", 1], [13, "double", 1], [23, "double", 2], [123, "double", 2]]
	if event == "bonda" or event == "so" or event == "bb":
		return run
	elif event == "triple":
		return count_run(runner)
	else:
		for i in range(10):
			if event == ore_run[i][1] and runner == ore_run[i][0]:
				run = ore_run[i][2]
				break
		return run

#得点期待値表への書き込みを行う関数、count_status= outcount, runner, 
def run_expection(or_memo):
	for i in range(len(or_memo)):
		count_status[or_memo[i][0]][or_memo[i][1]][or_memo[i][3] - or_memo[i][2]] += 1

#打者別得点期待値表への書き込みを行う関数、count_status_order= runner, outcount, runner, 
def run_expection_order(or_memo_order):
	for i in range(len(or_memo_order)):
		count_status_order[or_memo_order[i][0] - 1][or_memo_order[i][1]][or_memo_order[i][2]][or_memo_order[i][4] - or_memo_order[i][3]] += 1



def game(setting, game_counter, result):
    _result = result.game_results[game_counter]
    _result.run = 3

    #初期化
	inning, outcount, runner, order = [1, 0, 0, 1]
	run_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	or_memo = []
	or_memo_order = []

    while inning <= setting.INNING:
		#得点期待値表制作用、[アウトカウント、ランナー、その時点でのイニング得点数、最後の０はイニング終了時の得点]
		or_memo.append([outcount, runner207(runner), run_list[inning - 1], 0])
		#打順別得点期待値表制作用、[打順要素を追加]
		# or_memo_order.append([order, outcount, runner207(runner), run_list[inning - 1], 0])
		#  print("%d番" % order)
		#関数『打者』と関数『走塁』を呼び出す
		event = str(batter(order, outcount, runner207(runner)))
		
		#LWTS
		before_outcount, before_runner = [outcount, runner207(runner)]
		#イベント前の得点期待値
		before_RE = RE[before_outcount][before_runner]
		#Nを数える
		LWTS_N[event206(event)] += 1
		
		outcount, runner, run, change_flg = run_move(outcount, runner, event, order, TRS, N)
		#LWTS
        after_RE = run if change_flg else run + RE[outcount][runner207(runner)]
		
		#イベント前後の得点期待値変動
		LWTS[event206(event)] += after_RE - before_RE
		
		#  print("%dout %drunner run(%d)" % (outcount, runner, run))
		order += 1 #打順を1つ進める
		if order == 10: order = 1
		run_list[inning - 1] += run #イニング得点を記録
		
		if change_flg:
			#or_memoの最後にイニング終了時得点を記録
			for i in range(len(or_memo)):
				or_memo[i][3] = run_list[inning - 1]
			for i in range(len(or_memo_order)):
				or_memo_order[i][4] = run_list[inning - 1]
			#得点期待値表への書き込み
			run_expection(or_memo)
			run_expection_order(or_memo_order)
			#初期化
			or_memo = []
			or_memo_order = []
			#次のイニングへ行く処理
			inning += 1
			#print(run_list)
			#print("///////////////////////")

	#9イニングでの得点を記録
	run_total = int(sum(run_list))
	return run_total