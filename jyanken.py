#じゃんけんアプリ
import streamlit as st

# タイトルを表示
st.title("じゃんけん")

#手を選んでもらう
choise=st.radio("手を選んでね",["グー","チョキ","パー"])

if st.button("勝負！！"):
    st.write(F"あなたは{choise}を出しました!")