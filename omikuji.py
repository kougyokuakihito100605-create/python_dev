#運勢をリスト化する
unsei=["大吉", "中吉", "小吉", "吉", "凶"]
#運勢をランダムに選ぶためにrandomモジュールをインポートする
import random
#randomモジュールのchoice関数を使って、運勢をランダムに選ぶ
result=random.choice(unsei)
#選んだ運勢を表示する
print("今日の運勢は", result, "です。")