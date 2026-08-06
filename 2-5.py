#コンテナの応用
scores={'network':60,'database':80,'security':60}
members=['松田','麻木','工藤']
#リストmembersをタプルに変換して表示
print(tuple(members))
#scoresのキーをリストに変換して表示
print(list(scores))
#scoresの値をセットに変換して表示
print(set(scores.values()))

#ディクショナリへの変換は dict(zip(キー,値))

#ディクショナリの中にディクショナリをネスト
matsuda_scores={'network':60,'database':80,'security':50}
asagi_scores={'network':80,'database':75,'security':92}
member_scores={'松田':matsuda_scores,'麻木':asagi_scores}
print(member_scores)

#ディクショナリの中にセットをネスト
member_hobbies={'松田':{'SNS','麻雀','自転車'},'麻木':{'麻雀','食べ歩き','数学'}}
#全員の趣味一覧を表示する
print(member_hobbies)
#松田さんの趣味を表示する
print(member_hobbies['松田'])
#麻木さんの趣味を表示する
print(member_hobbies['麻木'])

#二次元リストの例
a=[1,2,3]
b=[4,5,6]
#ａを0番目、ｂを1番目とする２次元リストｃを定義
c=[a,b]
#リスト全体を表示
print(c)
#リストｃの0番目を表示
print(c[0])
#リストｃの１番目（リストｂ）の２番目を表示
print(c[1][2])

#セットの共通項を求める
member_hobbies={'松田':{'SNS','麻雀','自転車'},'麻木':{'麻雀','食べ歩き','数学'}}
common_hobbies=member_hobbies['松田']&member_hobbies['麻木']
#二人に共通する趣味一覧を表示する
print(common_hobbies)

#４つの集合演算
A={1,2,3,4}
B={2,3,4,5}
#和集合
print(A|B)
#積集合
print(A&B)
#差集合
print(A-B)
#対称差
print(A^B)
