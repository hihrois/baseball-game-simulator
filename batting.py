import csv
from numpy import random 
from setting import *

batting_stats = []

def read_batting_stats(file_name):
    """
    function: csvから打撃成績を読み込む
    input: csvファイルのパス(string)
    output: 打撃成績を確率に変換したもの（2次元list）
    """
    global batting_stats

    with open(file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            batting_stats.append(convert_batting_stats_to_probability(list(map(int, row))))

    return 0

def convert_batting_stats_to_probability(batting_stats):
    """
    function: 打撃成績を確率に変換する
    input: 打撃成績(list)
    output: 打撃成績を確率に変換したもの（list）
    """

    if len(batting_stats) != 7:
        raise Exception("打撃成績が正しく入力されていません")

    # batting_stats = [打席、総安打、二塁打、三塁打、本塁打、四死球、三振] を
    # probability = ["single_hit", "two_base_hit", "three_base_hit", "homerun", "walk_or_hit_by_pitch", "strike_out", "others"] に変換

    probability = [batting_stats[1] - (batting_stats[2] + batting_stats[3] + batting_stats[4]), batting_stats[2], batting_stats[3], batting_stats[4], batting_stats[5], batting_stats[6], batting_stats[0] - (batting_stats[1] + batting_stats[5] + batting_stats[6])]
    probability = list(map(lambda x: x / batting_stats[0], probability))
    
    return probability

def simulate_batting_result(batting_order, outcount, runner):
    """
    function: 打撃結果を出力する
    input: 打順(int)，アウトカウント(int)，ランナー(list)
    output: 打撃結果(string)
    """
    event = ["single_hit", "two_base_hit", "three_base_hit", "homerun", "walk_or_hit_by_pitch", "strike_out", "others"]
    batting_result = random.choice(event, p = batting_stats[batting_order - 1])

    return batting_result
