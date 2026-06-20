#運勢をリスト化する
unsei=["大吉", "中吉", "小吉", "吉", "凶"]

#それぞれの運勢に重みを付ける（合計100だとわかりやすい）
#大吉40％、中吉25％、小吉20％、吉10％、凶5％
weights=[40,25,20,10,5]

#運勢をランダムに選ぶためにrandomモジュールをインポートする
import random

#randomモジュールのchoices関数を使って、運勢をランダムに選ぶ
result=random.choices(unsei,weights=weights,k=1)[0]

#選んだ運勢を表示する
print("今日の運勢は", result, "です。")