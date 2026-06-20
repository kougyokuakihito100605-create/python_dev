#じゃんけんアプリ
import streamlit as st
import random  # 1. ライブラリを追加

st.title("じゃんけん")

# 手のリストを作成
hands = ["グー", "チョキ", "パー"]

# 手を選んでもらう
choice = st.radio("手を選んでね", hands)

if st.button("勝負！！"):
    # 2. CPUの手をランダムに決定
    cpu_hand = random.choice(hands)
    
    # 3. 結果を表示
    st.write(f"あなたは {choice} を出しました！")
    st.write(f"相手は {cpu_hand} を出しました！")
    
    # 4. 勝敗判定
    if choice == cpu_hand:
        st.write("結果：あいこ！")
    elif (choice == "グー" and cpu_hand == "チョキ") or \
         (choice == "チョキ" and cpu_hand == "パー") or \
         (choice == "パー" and cpu_hand == "グー"):
        st.write("結果：あなたの勝ち！🎉")
    else:
        st.write("結果：あなたの負け…😢")