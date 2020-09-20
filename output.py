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

    def output_result(self, setting):
        dt_now = datetime.datetime.now()
        dt_now = dt_now.strftime('%Y%m%d%H%M%S')
        with open(setting.OUTPUT_FILE_NAME.replace("time", dt_now), 'w', newline="") as f:
            writer = csv.writer(f)
            for output in self.output_array: writer.writerow([output.index_name, output.index])