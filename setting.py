import datetime
import os


class Setting:
    def __init__(self, delta_dependency_1B_BB, delta_wOBA, approach_parameter, output_directory):
        dt_now = datetime.datetime.now()
        dt_now = dt_now.strftime('%m%d%H%M%S')

        parameter = str(delta_dependency_1B_BB) + '_' + str(delta_wOBA) + '_' + str(approach_parameter)

        # input file path
        self.BATTING_STATS_FILE_NAME = "batting_stats/sample.csv"
        self.PITCHING_STATS_FILE_NAME = "input/pitching_stats/sample.csv"
        self.BASE_STATS_FILE_NAME = "input/base_stats/converted_stat"

        # output file path  'output_files_{}'.format(dt_now)
        self.OUTPUT_FOLDER_NAME = output_directory + '/' + parameter
        self.OUTPUT_FILE_NAME = self.OUTPUT_FOLDER_NAME + "/mean.csv"
        self.OUTPUT_FILE_NAME_RE = self.OUTPUT_FOLDER_NAME + "/re.csv"
        self.OUTPUT_FILE_NAME_RP = self.OUTPUT_FOLDER_NAME + "/rp.csv"
        self.OUTPUT_FILE_NAME_RE_ORDER = self.OUTPUT_FOLDER_NAME + "/re_order.csv"
        self.OUTPUT_FILE_NAME_RP_ORDER = self.OUTPUT_FOLDER_NAME + "/rp_order.csv"

        # game option
        self.NUM_OF_GAMES = 100000
        self.INNING = 9

        # log5
        # log5による補正を有効にするためには，PITCHING_STATS_FILE_NAMEとBASE_STATS_FILE_NAMEを入力してください
        self.DO_APPLY_LOG5 = False

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
