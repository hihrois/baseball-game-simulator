class Setting:
    def __init__(self):
        # batting stats
        self.BATTING_STATS_FILE_NAME = "batting_stats/sample.csv"
        self.OUTPUT_FILE_NAME = "output_files/output_time.csv" # timeの部分が時刻に変換されます
        
        # game option
        self.NUM_OF_GAMES = 100
        self.INNING = 9

        # indicate option
        self.IS_INDICATED_BOX_RESULT = False
        self.IS_INDICATED_GAME_RESULT = False