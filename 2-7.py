#練習問題(1)
scores=[80,60,75,82,30]
print(sum(scores))
print(sum(scores)/5)

#練習問題(2)
a={'麻雀','勉強','読書','食べ歩き','パチンコ'}
b={'パチンコ','競馬','競輪','宝くじ','食べ歩き'}
input('心の準備が出来たらEnterキーを押してください>>')
aisyou=(len(a&b))/(len(a|b))*100
print(f'相性は、{aisyou}%です。')

