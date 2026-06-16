#練習問題1-1
print(2+10*5)
print('7'*(3+4))
print(f'version{3+2*0.1+9*0.01}')
print(4*'num'+'回目のtypeError')

#練習問題1-2
num=2
var=35+num
num+=5
GLOBAL='世界'+str(num)+'カ国'
check_code=num*(9/3)
print(type(GLOBAL))
print(type(check_code))

#練習問題1-3　BMIを求めるプログラム
kg=int(input('あなたの体重を入力してください＞＞'))
cm=float(input('あなたの身長を入力してください＞＞'))
cm=cm/100
BMI=kg/cm/cm
print(f'あなたのBMIは{round(BMI)}です')