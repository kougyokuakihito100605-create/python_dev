#データ型
price=input('料金を入力＞＞') #文字列になる
number=input('人数を入力＞＞')
#データ型を調べる
print(type(price))
print(type(number))

#データ型の変換
x=3.14
y=int(x) 
print(y) #変換結果を表示
print(type(y)) #変換後のデータ型を表示
z=str(x)
print(z) #変換結果を表示
print(type(z)) #変換後のデータ型を表示
print(z*2)

#割り勘計算プログラム1
price=input('料金を入力＞＞')
price=int(price)
number=input('人数を入力＞＞')
number=int(number)
payment=price/number
payment=int(payment)
print('お支払いは'+str(payment)+'円です')

#文字列に数値を埋め込む(fornat関数)
name='工藤樹'
age=35
height=152.5
print('私の名前は{}で、年齢は{}歳、身長{}㎝です'.format(name,age,height))

#割り勘計算プログラム2
price=int(input('料金を入力＞＞'))
number=int(input('人数を入力＞＞'))
payment=int(price/number)
print('お支払いは{}円です'.format(payment))

#文字列に数値を埋め込む(f-string)
name='工藤樹'
age=35
height=152.5
print(f'私の名前は{name}で、年齢は{age}歳、身長{height}㎝です')