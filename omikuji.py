#おみくじアプリ
import streamlit as st
import random

# タイトルを表示
st.title("⛩️ デジタルおみくじ")

#ボタンを作成
if st.button('おみくじを引く'):
    #運勢をリスト化する
    unsei=["大吉", "中吉", "小吉", "吉", "凶"]

    #それぞれの運勢に重みを付ける（合計100だとわかりやすい）
    #大吉40％、中吉25％、小吉20％、吉10％、凶5％
    weights=[40,25,20,10,5]

    #randomモジュールのchoices関数を使って、運勢をランダムに選ぶ
    result=random.choices(unsei,weights=weights,k=1)[0]

    #選んだ運勢を表示する
    st.header(f"今日の運勢は... 「{result}」です！")

    #大吉の時だけの演出
    if result=="大吉":
       st.balloons()
       st.success("おめでとうございます！、今日もよい一日になりますように")
       
#http://localhost:8501
#http://172.31.25.141:8501