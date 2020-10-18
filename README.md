# baseball-game-simulator
baseball-game-simulator is practical baseball simulating tool.  
You can make unlimited patterns of batting order, and simulate it.  
This project has just begun and is not matured.  
Please don't hesitate to join our project and edit codes!  

# Usage
## 1. Edit setting.py
You need to set variables first. (e.g. number of games, number of innings, etc..)  
Open "setting.py" and edit it in your own.  

## 2. Edit batting_stats
Second, you need to set batting stats.  
Make a new .csv file (/batting_stats/) and write batting stats in it.  
  
In the simulator, players' ability is expressed as 7 dimensional vector.  
The vector is consists of (number of) plate appearences, (all) hits, doubles, triples, homeruns, walk and hit by pitches, and knock outs.  
batting_stats/sample.csv exsits initially, so refer it when you want to know about it.  
  
Be sure to change the valuable "BATTING_STATS_FILE_NAME" (in setting.py) correctly when you make a new .csv file.  

## 3. Simulate
If you finish setting up, it is time to simulate!  
Open your terminal and execute command "python main.py".

## 4. See the results
If the program has finished, let's check the results.  
The results file is generated in /output_files/ automatically.  
Initially, average runs and standard deviation are available.  

(Sorry for poor. That is one of the function we should update soon... You can expand it yourself, of course.)

# Author
Let me(twitter: @3I1zmPds0weQwYm) know if you have any questions!
