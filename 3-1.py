#例文
name=input('あなたの名前を教えてください>>')
print(F'{name}さん、こんにちは')
food=input(F'{name}さんの好きな食べ物を教えてください>>')
print(F'私も{food}が好きですよ')

#IF文
name=input('あなたの名前を教えてください>>')
print(F'{name}さん、こんにちは')
food=input(F'{name}さんの好きな食べ物を教えてください>>')
if food == 'カレー':
    print('素敵です。カレーは最高ですよね')
else:
    print(F'私も{food}が好きですよ')

#点数判定プログラム
score=int(input('試験の点数を入力してください>>'))
if score >= 60:
    print('合格！')
    print('よく頑張りました')
else:
    print('もう少し頑張りましょう')
    print('追試を受けてください')
