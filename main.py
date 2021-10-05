import setting
import result
from simulate import *
import batting
import output

FILE_PATH = './batting_stats/converted_stat'

wOBA_COEFFICIENT = {
    'BB': 0.7
    ,'1B': 0.9
    ,'2B': 1.3
    ,'3B': 1.3
    ,'HR': 2.0
}

delta_dependency_1B_BB_list = [0.1, 0.2, 0.3, 0.4]
delta_wOBA_list = [-0.005]
# delta_wOBA_list = [0, -0.01, -0.02, -0.03, -0.04, -0.05]

# アプローチ方針パラメータ
"""
1: ノーマル固定
2: 出塁固定
3: 長打固定
4: 使い分け
"""
# approach_parameter = 1


from time import sleep
def adjust_minus_probability(batting_stat):
    for batting_slot in range(9):
        for x in batting_stat[batting_slot]:
            if x < 0:
                print('minus probability found: {}'.format(batting_stat[batting_slot]))
        batting_stat[batting_slot] = list(map(lambda x: max(0, x), batting_stat[batting_slot]))
        if sum(batting_stat[batting_slot]) != 1:
            batting_stat[batting_slot] = list(map(lambda x: x / sum(batting_stat[batting_slot]), batting_stat[batting_slot]))
    
    return batting_stat


def compute_wOBA(batting_stat):
    for i in range(9):
        wOBA = wOBA_COEFFICIENT['1B'] * batting_stat[i][0] + wOBA_COEFFICIENT['2B'] * batting_stat[i][1] \
            + wOBA_COEFFICIENT['3B'] * batting_stat[i][2] + wOBA_COEFFICIENT['HR'] * batting_stat[i][3] \
            + wOBA_COEFFICIENT['BB'] * batting_stat[i][4]

        print('{}: wOBA {}'.format(i + 1, wOBA))


# 打撃成績の読み込み
with open(FILE_PATH, 'rb') as file:
    individual_stat = pickle.load(file)

dt_now = datetime.datetime.now()
dt_now = dt_now.strftime('%m%d%H%M%S')
output_directory = 'output_files_{}'.format(dt_now)
os.makedirs(output_directory)

for approach_parameter in range(1, 5):
    approach_parameter = 4
    for delta_dependency_1B_BB in delta_dependency_1B_BB_list:
        for delta_wOBA in delta_wOBA_list:
            # delta_dependency_1B_BB = key[0]
            # delta_wOBA = key[1]
            # batting_stat = value

            # 各アプローチの制約を格納
            batting_stat_normal = individual_stat[0, 0]
            batting_stat_on_base = individual_stat[delta_dependency_1B_BB, delta_wOBA]
            batting_stat_on_long_hit = individual_stat[-delta_dependency_1B_BB, delta_wOBA]

            # 最小値を0に補正
            batting_stat_normal = adjust_minus_probability(batting_stat_normal)
            batting_stat_on_base = adjust_minus_probability(batting_stat_on_base)
            batting_stat_on_long_hit = adjust_minus_probability(batting_stat_on_long_hit)

            print('delta_dependency_1B_BB: {}'.format(delta_dependency_1B_BB))
            print('delta_wOBA: {}'.format(delta_wOBA))
            
            # 成績確認
            print('batting_stat_normal')
            compute_wOBA(batting_stat_normal)
            print('batting_stat_on_base')
            compute_wOBA(batting_stat_on_base)
            print('batting_stat_on_long_hit')
            compute_wOBA(batting_stat_on_long_hit)

            # クラス宣言
            setting_ = setting.Setting(delta_dependency_1B_BB, delta_wOBA, approach_parameter, output_directory)
            batting_ = batting.Batting(setting_.PITCHING_STATS_FILE_NAME, setting_.BASE_STATS_FILE_NAME, setting_.BATTING_STATS_FILE_NAME, setting_)
            result_ = result.Result(setting_.NUM_OF_GAMES)
            output_ = output.Output()

            # シミュレート
            simulate(setting_, batting_, batting_stat_normal, batting_stat_on_base, batting_stat_on_long_hit, approach_parameter, result_, output_)

            # 結果の集計
            result_.aggregate_result(setting_, output_)

            # 結果の出力
            output_.output_result(setting_)
            output_.output_re(setting_)
            output_.output_rp(setting_)
    sys.exit()

