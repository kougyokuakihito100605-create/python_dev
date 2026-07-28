#タプルとセット
#タプルは要素の追加、変更、削除ができない
scores=(70,80,55)
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')

#要素の変更とエラー
#scores=(70,80,55)
#scores[0]=80

#要素数1のリスト
members=['松田']
#要素1のディクショナリ
scores={'network':82}
#要素1のタプルのつもり
members=('松田')
print(type(members))
#要素1のタプルの正しい定義
members=('松田',)
print(type(members))

#セットは種類を管理するのに向いている
#セットの利用
scores={70,80,55,80}
scores.add(80)
print(scores)
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')