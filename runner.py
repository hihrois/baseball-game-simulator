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
    next_runner = trs_runner_list[trs_rst]

    #得点計算(アウトカウントとランナーの数+1から、次のアウトカウントと次のランナーを引いた数が得点になる)
	#チェンジ判定
	change_flg = 0
	if outcount > next_outcount:
		run = run_and_change_cal(runner, event)
		global left
		left += count_run(runner) - run
		change_flg = 1
	else :
		run = outcount + count_run(runner) + 1 - next_outcount - count_run(next_runner)
	
    return [next_outcount, next_runner, run, change_flg]