import csv
from numpy import random 
from setting import *
import sys


class Batting:
    def __init__(self, file_name_pitching, file_name_base, file_name_batting, setting):
        self.pitching_stats = self.read_pitching_stats(file_name_pitching, setting)
        self.base_stats = self.read_pitching_stats(file_name_base, setting)
        self.batting_stats = self.read_batting_stats(file_name_batting, setting)

    def read_batting_stats(self, file_name, setting):
        """
        function: csvから打撃成績を読み込む
        input: csvファイルのパス(string)
        output: 打撃成績を確率に変換したもの（2次元list）
        
        打席数，総安打数，二塁打，三塁打，本塁打，四死球，三振の各確率
        """
        batting_stats = []
        with open(file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                # batting_stats.append(self.convert_batting_stats_to_probability(list(map(int, row))))
                probability_list = self.convert_batting_stats_to_probability(list(map(int, row)))
                if setting.DO_APPLY_LOG5:
                    probability_list = self.apply_log5(probability_list)
                batting_stats.append(probability_list)

        return batting_stats

    def read_pitching_stats(self, file_name, setting):
        if not setting.DO_APPLY_LOG5: return
        with open(file_name) as f:
            reader = csv.reader(f)
            for row in reader:
                return self.convert_batting_stats_to_probability(list(map(int, row)))


    def convert_batting_stats_to_probability(self, batting_stats):
        """
        function: 打撃成績を確率に変換する
        input: 打撃成績(list)
        output: 打撃成績を確率に変換したもの（list）
        """
        NUM_OF_BATTING_STATS_COLUMNS = 7

        if len(batting_stats) != NUM_OF_BATTING_STATS_COLUMNS:
            raise Exception("打撃成績が正しく入力されていません")

        probability = [
            batting_stats[1] - (batting_stats[2] + batting_stats[3] + batting_stats[4]), 
            batting_stats[2], 
            batting_stats[3], 
            batting_stats[4], 
            batting_stats[5], 
            batting_stats[6], 
            batting_stats[0] - (batting_stats[1] + batting_stats[5] + batting_stats[6])
        ]

        probability = list(map(lambda x: x / batting_stats[0], probability))
        
        return probability

    
    def apply_log5(self, probability):
        def odds(x):
            return x / (1 - x)

        def log5(a, b, l):
            return odds(a) / (odds(l) * odds(b))
        
        def convert_odds_to_p(odds):
            return odds / (1 + odds)

        output = []

        # hit系
        for i in range(5):
            output.append(convert_odds_to_p(log5(probability[i], 1 - self.pitching_stats[i], self.base_stats[i])))

        # 三振系
        output.append(convert_odds_to_p(log5(self.pitching_stats[5], 1 - probability[5], self.base_stats[5])))

        # 凡打
        output.append(convert_odds_to_p(log5(probability[6], 1 - self.pitching_stats[6], self.base_stats[6])))
        
        output_sum = sum(output)
        output = list(map(lambda x: x/output_sum, output))

        return output


    def simulate_batting_result(self, batting_order, batting_stats, outcount, runner):
        """
        function: 打撃結果を出力する
        input: 打順(int)，アウトカウント(int)，ランナー(list)
        output: 打撃結果(string)
        """
        event = ["single", "double", "triple", "hr", "bb", "so", "bonda"]
        batting_result = random.choice(event, p = batting_stats[batting_order - 1])

        return batting_result
