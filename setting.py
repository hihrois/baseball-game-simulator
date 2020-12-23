import datetime
import os

class Setting:
    def __init__(self):
        dt_now = datetime.datetime.now()
        dt_now = dt_now.strftime('%Y%m%d%H%M%S')
        
        # batting stats
        self.BATTING_STATS_FILE_NAME = "batting_stats/sample.csv"
        self.OUTPUT_FOLDER_NAME = "output_files/result_{}/".format(dt_now)
        self.OUTPUT_FILE_NAME = self.OUTPUT_FOLDER_NAME + "mean.csv"
        self.OUTPUT_FILE_NAME_RE = self.OUTPUT_FOLDER_NAME + "re.csv" 
        self.OUTPUT_FILE_NAME_RE_ORDER = self.OUTPUT_FOLDER_NAME + "re_order.csv" 
        
        # game option
        self.NUM_OF_GAMES = 10000
        self.INNING = 9

        # RE
        self.DO_COMPUTE_RE = True
        self.DO_COMPUTE_RE_ORDER = True

        # ターミナル表示オプション
        self.IS_INDICATED_BOX_RESULT = False
        self.IS_INDICATED_GAME_RESULT = False

        os.makedirs(self.OUTPUT_FOLDER_NAME)