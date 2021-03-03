# baseball-game-simulator
実用的な野球のシミュレーションツールです．  
打撃成績，打順，投手能力など，様々な条件を設定してシミュレーションを行うことができます．  
シミュレーションの仕組みについては以下のブログをご覧ください．  
https://hihrois-1104o.hatenablog.com/entry/yakyuu-simyu-detail     

# Usage
## 1. Edit setting.py
まずはじめにパラメータを設定します（シミュレーションする試合数，試合のイニング等）．  
`~/setting.py`を編集してください．  

## 2. Edit input
### 2-1. batting_stats
次に，打撃成績を入力します．  
`~/batting_stats/`にcsvファイルを作成し，打撃成績を書き込んでください．  

シミュレーション内では，打者の能力は7次元の情報で表現されます．  
打席数，総安打数，二塁打，三塁打，本塁打，四死球，三振です．  
サンプルファイルは`~/batting_stats/sample.csv`においてあるので，詳しい書き方はこちらをご参照ください．  

打撃成績のファイルパスは`setting.py`内の"BATTING_STATS_FILE_NAME"で設定してください．  


### 2-2. pitching_stats, base_stats (optional)
打者と投手の能力から妥当な対戦結果を推定するlog5モデルを使用する場合，投手成績とリーグ平均成績を入力する必要があります．  
投手成績とリーグ平均成績の入力方法は打撃成績と同じです．  

## 3. Simulate
これで準備は終了です．  
ターミナルから`python main.py`を実行してください．  

## 4. See the results
プログラムが無事に終了したら，結果ファイルを確認します．  
結果ファイルは`~/output_files/`に生成されます．  

# Author
何か質問などございましたら，[@bb_analy](https://twitter.com/bb_analy)までご連絡ください！

    
# baseball-game-simulator(English)
baseball-game-simulator is practical baseball simulating tool.  
You can make unlimited patterns of batting order, and simulate it.   

If you want to know the details, please visit my blog!　(Japanese only)  
https://hihrois-1104o.hatenablog.com/entry/yakyuu-simyu-detail   

# Usage
You need to set variables first. (e.g. number of games, number of innings, etc..)  
Open `~/setting.py` and edit it on your own.  

## 2. Edit input
### 2-1. batting_stats
Second, you need to set batting stats.  
Make a new .csv file and write batting stats in `~/batting_stats/`.  
  
In the simulator, players' ability is expressed as 7 dimensional vector.  
The vector is consists of (number of) plate appearences, (all) hits, doubles, triples, homeruns, walk and hit by pitches, and knock outs.  
`~/batting_stats/sample.csv` exsits initially. Please refer to it when you want to know about it.  
  
Be sure to change the valuable "BATTING_STATS_FILE_NAME" (in `setting.py`) correctly when you make a new .csv file. 

### 2-2. pitching_stats, base_stats (optional)
When applying log5 model, you need to add pitching_stats and base_stats.  
pitching_stats is stats of opponents'pitcher, and the construction is same with batting_stats.  
base_stats is stats of average pitcher(batter), the construction is also consistent with batting stats and pitching stats.  

## 3. Simulate
If you finish setting up, it is time to simulate!  
Open your terminal and execute command `python main.py`.

## 4. See the results
let's check the results after finishing program.  
The results file is generated in `~/output_files/` automatically.  
Some stats are available (e.g. average run, sd, RE table,...).  

# Author
Let me(twitter: [@bb_analy](https://twitter.com/bb_analy)) know if you have any questions!　
