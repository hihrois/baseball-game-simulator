import setting
import result
from simulate import *
import batting
import output

# クラス宣言
setting = setting.Setting()
batting = batting.Batting(setting.PITCHING_STATS_FILE_NAME, setting.BASE_STATS_FILE_NAME, setting.BATTING_STATS_FILE_NAME, setting)
result = result.Result(setting.NUM_OF_GAMES)
output = output.Output()

# シミュレート
simulate(setting, batting, result, output)

# 結果の集計
result.aggregate_result(setting, output)

# 結果の出力
output.output_result(setting)
output.output_re(setting)
output.output_rp(setting)

run_list = output.re_order_tmp
parameter = [0, 0, 0]
max_CI = -1

for batting_order in range(9):
    for outcount in range(3):
        for runner in range(8):
            tmp_array = run_list[batting_order][outcount][runner]

            print("打順 {}, アウト {}, ランナー {}".format(batting_order + 1, outcount, runner))

            mean = 0
            N = sum(tmp_array)
            print("N: {}".format(N), end=" ")
            for i in range(30):
                mean += i * tmp_array[i]
            mean /= N
            print("mean: {}".format(mean), end=" ")

            ud = 0
            for i in range(30):
                ud += (i - mean) ** 2 * tmp_array[i]
            ud /= N - 1

            print("ud: {}".format(ud), end=" ")

            from scipy.stats import t
            from math import sqrt
            p_975 = t.ppf(0.975, N - 1)
            CI = sqrt(ud)/sqrt(N) * p_975

            if CI > max_CI:
                max_CI = CI
                parameter = [batting_order + 1, outcount, runner]

            print("信頼区間: +-{}".format(CI))

print("max_CI: +-{}".format(max_CI))
print(*parameter)