import setting
import result
from simulate import *
import output

# クラス宣言
setting = setting.Setting()
result = result.Result(setting.NUM_OF_GAMES)
output = output.Output()

# シミュレート
simulate(setting, result)

# 結果の集計
result.aggregate_result(setting, output)

# 結果の出力
output.output_result(setting)