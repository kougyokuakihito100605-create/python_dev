#ディクショナリ
scores={'network':60,'database':80,'security':50}
print(scores)

#ディクショナリ要素の参照
print(scores['database'])

#ディクショナリ要素の追加と変更
scores['programming']=65
scores['security']=55
print(scores)

#ディクショナリ要素の削除
del scores['security']
print(scores)

#ディクショナリの合計
scores={'network':60,'database':80,'security':50}
total=sum(scores.values())
print(total)