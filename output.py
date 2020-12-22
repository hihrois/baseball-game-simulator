import csv
import datetime

class Output:
    class index:
        def __init__(self, _id, index_name, index):
            self.id = _id
            self.index_name = index_name
            self.index = index # 型は int, float, もしくは int, float の配列のみ

    def __init__(self):
        self.output_array = []
        self.re_tmp = [[[0 for i in range(30)] for i in range(8)] for i in range(3)]
        self.re_order_tmp = [[[[0 for i in range(30)] for i in range(8)] for i in range(3)]for i in range(9)]
        self.re = [[] for _ in range(3)]
        self.re_order = [[[] for _ in range(3)] for _ in range(9)]

    # 得点期待値表への書き込みを行う関数
    def write_re_tmp(self, or_memo):
        for i in range(len(or_memo)):
            self.re_tmp[or_memo[i][0]][or_memo[i][1]][or_memo[i][3] - or_memo[i][2]] += 1

    # 打者別得点期待値表への書き込みを行う関数
    def write_re_order_tmp(self, or_memo_order):
        for i in range(len(or_memo_order)):
            self.re_order_tmp[or_memo_order[i][0] - 1][or_memo_order[i][1]][or_memo_order[i][2]][or_memo_order[i][4] - or_memo_order[i][3]] += 1

    # 結果をcsvに書き込み
    def output_result(self, setting):
        with open(setting.OUTPUT_FILE_NAME, 'w', newline="") as f:
            writer = csv.writer(f)
            for output in self.output_array:
                writer.writerow([output.index_name, output.index])

    # 得点期待値表をcsvに書き込み
    def output_re(self, setting):
        if setting.DO_COMPUTE_RE:
            with open(setting.OUTPUT_FILE_NAME_RE, 'w', newline="") as f:
                writer = csv.writer(f)
                for outcount in range(3):
                    writer.writerow([round(run, 3) for run in self.re[outcount]])
                    
        if setting.DO_COMPUTE_RE_ORDER:
            with open(setting.OUTPUT_FILE_NAME_RE_ORDER, 'w', newline="") as f:
                writer = csv.writer(f)
                for batting_order in range(9):
                    for outcount in range(3):
                        writer.writerow([round(run, 3) for run in self.re_order[batting_order][outcount]])