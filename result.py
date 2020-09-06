import statistics

class Result:
    class GameResult:
        def __init__(self):
            self.run = None

    def __init__(self, NUM_OF_GAMES):
        self.game_results = [Result.GameResult()] * NUM_OF_GAMES

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