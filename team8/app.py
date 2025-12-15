import streamlit as st
from pathlib import Path
from PIL import Image

# ===== 基本設定 =====
BASE_DIR = Path(__file__).parent

if "page" not in st.session_state:
    st.session_state.page = "home"

if "starter" not in st.session_state:
    st.session_state.starter = None


# ===== 画像表示 =====
def show_image(filename):
    path = BASE_DIR / filename
    image = Image.open(path)
    st.image(image, use_column_width=True)


# ===== 御三家選択画面 =====
def home():
    st.title("ポケモンSV｜初心者限定攻略サイト")
    st.write("どの御三家を選んでも大丈夫。楽しむことが一番です。")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_image("sprigatito.png")
        if st.button("ニャオハ"):
            st.session_state.starter = "ニャオハ"
            st.session_state.page = "story"

    with col2:
        show_image("fuecoco.png")
        if st.button("ホゲータ"):
            st.session_state.starter = "ホゲータ"
            st.session_state.page = "story"

    with col3:
        show_image("quaxly.png")
        if st.button("クワッス"):
            st.session_state.starter = "クワッス"
            st.session_state.page = "story"


# ===== 攻略画面 =====
def story():
    starter = st.session_state.starter

    st.title(f"{starter} を選んだ人向け攻略")

    st.markdown("""
### 🎮 このサイトの考え方
- 負けてもOK  
- レベルを上げれば必ず進める  
- 好きなポケモンを使っていい
""")

    # ===== レベル入力 =====
    level = st.slider("手持ちポケモンの平均レベル", 1, 60, 10)

    # ===== レベル別進行 =====
    st.markdown("## 🗺 今おすすめの進行")

    if level <= 15:
        st.info("最初の草原エリア → 虫ジム")
    elif level <= 25:
        st.info("草ジム → 水ジム")
    else:
        st.info("中盤以降のジム・スター団・レイド")

    # ===== マップ =====
    show_image("sv_map_all.png")

    # ===== 御三家別アドバイス =====
    st.markdown("## ⭐ 御三家別アドバイス")

    if starter == "ニャオハ":
        st.warning("🔥 炎・虫ジムに注意")
        st.write("おすすめ仲間：パモ、ウパー")

    elif starter == "ホゲータ":
        st.warning("💧 水ジムに注意")
        st.write("おすすめ仲間：マリル、シェルダー")

    elif starter == "クワッス":
        st.warning("⚡ 電気・草ジムに注意")
        st.write("おすすめ仲間：ウパー、ディグダ")

    # ===== 戻る =====
    if st.button("御三家選択に戻る"):
        st.session_state.page = "home"


# ===== 画面制御（ここだけ） =====
if st.session_state.page == "home":
    home()
elif st.session_state.page == "story":
    story()
