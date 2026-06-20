#ディクショナリ
scores={'network':60,'database':80,'security':50}
car={'maker':'daihatu','model':'move','color':'green'}
print(scores)
print(car)

#ディクショナリ要素の参照
print(scores['database'])
print(car['color'])

#ディクショナリ要素の追加と変更
scores['programming']=65
car['model']='tanto_custom'
scores['security']=55
car['money']=1000000
print(scores)
print(car)

#ディクショナリ要素の削除
del scores['security']
print(scores)
del car['maker']
print(car)

#ディクショナリの合計
scores={'network':60,'database':80,'security':50}
total=sum(scores.values())
print(total)