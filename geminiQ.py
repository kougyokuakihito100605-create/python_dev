#リストの基本操作とスライス
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#末尾に"fig"を追加する
fruits.append("fig")
print(fruits)
#リストの取得と変数への代入
some_fruits=(fruits[:3])
print(some_fruits)

#ディクショナリの操作
scores = {"math": 85, "english": 90, "science": 78}
#'history'を追加する
scores['history']=92
print(scores)
#'english'の点数を更新する
scores['english']=95
print(scores)
#ディクショナリをリストに変換
print(list(scores))

#セット（集合）を使った重複の削除
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
#重複を取り除いてセットへ変換する
unique_numbers = set(numbers)
print(unique_numbers)