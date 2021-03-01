import datetime
import os


class Setting:
    def __init__(self):
        dt_now = datetime.datetime.now()
        dt_now = dt_now.strftime('%Y%m%d%H%M%S')

        # input file path
        self.BATTING_STATS_FILE_NAME = "batting_stats/sample.csv"
        self.PITCHING_STATS_FILE_NAME = "input/pitching_stats/sample.csv"
        self.BASE_STATS_FILE_NAME = "input/base_stats/sample.csv"

        # output file path
        self.OUTPUT_FOLDER_NAME = "output_files/result_{}/".format(dt_now)
        self.OUTPUT_FILE_NAME = self.OUTPUT_FOLDER_NAME + "mean.csv"
        self.OUTPUT_FILE_NAME_RE = self.OUTPUT_FOLDER_NAME + "re.csv"
        self.OUTPUT_FILE_NAME_RP = self.OUTPUT_FOLDER_NAME + "rp.csv"
        self.OUTPUT_FILE_NAME_RE_ORDER = self.OUTPUT_FOLDER_NAME + "re_order.csv"
        self.OUTPUT_FILE_NAME_RP_ORDER = self.OUTPUT_FOLDER_NAME + "rp_order.csv"

        # game option
        self.NUM_OF_GAMES = 10000
        self.INNING = 9

        # log5
        # log5による補正を有効にするためには，PITCHING_STATS_FILE_NAMEとBASE_STATS_FILE_NAMEを入力してください
        self.DO_APPLY_LOG5 = True

        # RE
        self.DO_COMPUTE_RE = True
        self.DO_COMPUTE_RE_ORDER = True

        # RP
        self.DO_COMPUTE_RP = True
        self.DO_COMPUTE_RP_ORDER = True

        # ターミナル表示オプション
        self.IS_INDICATED_BOX_RESULT = False
        self.IS_INDICATED_GAME_RESULT = False

        os.makedirs(self.OUTPUT_FOLDER_NAME)
