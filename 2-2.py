#リスト
members=['工藤','松田','麻木']
print(members)
print([members[0]])

#試験の合計と平均を求める
scores=[88,90,95]
total=scores[0]+scores[1]+scores[2]
print(f'合計{total}点')

#試験の合計と平均を求める2
scores=[88,90,95]
total=sum(scores)
print(f'合計{total}点')

#試験の合計と平均を求める3
scores=[88,90,95]
total=sum(scores)
avg=total/len(scores)
print(F'合計{total}点、平均{avg}点')

#リストに要素を追加
members=['工藤','松田','麻木']
members.append('菅原')
members.append('湊')
members.append('浅香')
print(members)

#リストから要素を削除
members=['工藤','松田','麻木']
members.remove('松田')
print(members)

#リストの要素を変更
members=['工藤','松田','麻木']
members[0]='菅原'
print(members)

#スライスによる範囲指定
a=[10,20,30,40,50]
print(a[1:3]) #インデックスが1以上3未満
print(a[2:]) #インデックスが2以上の全ての要素
print(a[:3]) #インデックスが3未満の全ての要素

#負の数による指定
a=[10,20,30,40,50]
print(a[-1]) #末尾の要素を参照
print(a[-2]) #末尾から2番目の要素を参照
