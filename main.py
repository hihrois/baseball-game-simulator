import setting
import result
from simulate import *
import batting
import output

# クラス宣言
setting = setting.Setting()
batting = batting.Batting(setting.BATTING_STATS_FILE_NAME)
result = result.Result(setting.NUM_OF_GAMES)
output = output.Output()

# シミュレート
simulate(setting, batting, result)

# 結果の集計
result.aggregate_result(setting, output)

# 結果の出力
output.output_result(setting)