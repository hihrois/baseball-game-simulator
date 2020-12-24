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

