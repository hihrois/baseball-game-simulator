# baseball-game-simulator
baseball-game-simulator is practical baseball simulating tool.  
You can make unlimited patterns of batting order, and simulate it.   

If you want to know the details, please visit my blog!　(Japanese only)  
https://hihrois-1104o.hatenablog.com/entry/yakyuu-simyu-detail

# Usage
## 1. Edit setting.py
You need to set variables first. (e.g. number of games, number of innings, etc..)  
Open `~/setting.py` and edit it on your own.  

## 2. Edit input
### 2-1. batting_stats
Second, you need to set batting stats.  
Make a new .csv file (`~/batting_stats/`) and write batting stats in it.  
  
In the simulator, players' ability is expressed as 7 dimensional vector.  
The vector is consists of (number of) plate appearences, (all) hits, doubles, triples, homeruns, walk and hit by pitches, and knock outs.  
`~/batting_stats/sample.csv` exsits initially. Prease refer to it when you want to know about it.  
  
Be sure to change the valuable "BATTING_STATS_FILE_NAME" (in setting.py) correctly when you make a new .csv file.  

### 2-2. pitching_stats, base_stats (optional)
When applying log5 model, you need to add pitching_stats and base_stats.  
pitching_stats is stats of opponents'pitcher, and the construction is the same with batting_stats.  
base_stats is stats of average pitcher, ofcourse, the construction is same.  

## 3. Simulate
If you finish setting up, it is time to simulate!  
Open your terminal and execute command "python main.py".

## 4. See the results
If the program has finished, let's check the results.  
The results file is generated in `~/output_files/` automatically.  
Some stats are available (e.g. average run, sd, RE table,...)

# Author
Let me(twitter: @bb_analy) know if you have any questions!
