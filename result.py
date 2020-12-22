import statistics

class Result:
    class GameResult:
        def __init__(self):
            self.run = None

    def __init__(self, NUM_OF_GAMES):
        self.game_results = [Result.GameResult() for _ in range(NUM_OF_GAMES)]

    # 集計関数
    def mean(self, run):
        return statistics.mean(run)
    
    def stdev(self, run):
        return statistics.stdev(run)

    # 結果の集計
    def aggregate_result(self, setting, output):
        # 得点を1次元リスト化
        run = []
        for game_result in self.game_results:
            run.append(game_result.run)
        
        output_list = [
            ("mean", self.mean(run)), 
            ("sd", self.stdev(run)),
        ]

        for _id, (index_name, index) in enumerate(output_list):
            output.output_array.append(output.index(_id, index_name, index))

        self.compute_re(output)
        self.compute_re_order(output)

    def compute_re(self, output):
        print("---------RE---------")
        for outcount in range(3):#アウトカウント
            for runner in range(8):#ランナー
                num_list = [0, 1, 2, 12, 3, 13, 23, 123]
                hoge = 0
                for i in range(30):
                    hoge += i * output.re_tmp[outcount][runner][i]
                if sum(output.re_tmp[outcount][runner]) == 0:
                    result = 0
                else:
                    result = hoge / sum(output.re_tmp[outcount][runner])
                    output.re[outcount].append(result)
                print("{}アウト {}ランナー　{}点".format(outcount, num_list[runner], result))
        print("")

    def compute_re_order(self, output):
        print("---------RE split by batting order---------")
        for batting_order in range(9):
            for outcount in range(3):#アウトカウント
                for runner in range(8):#ランナー
                    num_list = [0, 1, 2, 12, 3, 13, 23, 123]
                    hoge = 0
                    for k in range(30):
                        hoge += k * output.re_order_tmp[batting_order][outcount][runner][k]
                    if sum(output.re_order_tmp[batting_order][outcount][runner]) == 0:
                        result = 0
                    else:
                        result = hoge / sum(output.re_order_tmp[batting_order][outcount][runner])
                        output.re_order[batting_order][outcount].append(result)
                    print("{}番 {}アウト {}ランナー　{}点".format(batting_order + 1, outcount, num_list[runner], result))
        print("")