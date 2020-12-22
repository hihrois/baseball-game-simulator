1. outputファイルについて
mean: 平均得点
sd: 標準偏差
何を出力するかはresult.pyから編集可能です．

2.re（得点期待値表）ファイルについて
次のように出力されます．

0out run0のre, 0out run1のre, 0out run12のre, 0out run3のre, 0out run13のre, 0out run23のre, 0out run123のre, 
1out run0のre, 1out run1のre, 1out run12のre, 1out run3のre, 1out run13のre, 1out run23のre, 1out run123のre,
2out run0のre, 2out run1のre, 2out run12のre, 2out run3のre, 2out run13のre, 2out run23のre, 2out run123のre,

すなわち，行とアウトカウント，列とランナーがそれぞれ対応する形を取ります．
打者別(re_order)の場合は，上記の出力を1番打者から順に出力します．