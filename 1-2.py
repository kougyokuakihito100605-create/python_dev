#変数の利用
name='松田'
age=22
print(name)
print(age)

print('半径が3㎝の円の直径は')
dia=3*2
print(dia)
print('その円の円周の長さは、')
print(dia*3.14)

#変数の上書き
count=3
print('今日カレーを食べた回数は')
print(count)
count=5
print('うそ、本当は')
print(count)

#複数の変数をまとめて定義
name,age='麻木',24
print(name,age)

#麻木さんの年齢を予測するプログラム
age=24
print('麻木先輩の今の年齢は…')
print(age)
age=age+1
print('来年は…')
print(age)
age=age+1
print('再来年は…')
print(age)

#変数の現在の値に加減乗除する
age=24
age+=1

price=2600
price*=1.5

print(age)
print(price)

#キーボードから値を入力する
name=input('あなたの名前を入力してください>>')
print('おお'+name+'よ、そなたがくるのを待っておったぞ！')
