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


# ===== 御三家選択 =====
def select_starter():
    st.title("ポケモンSV 初心者攻略サイト")
    st.write("最初に選んだ御三家に合わせて、やさしい攻略を案内します。")

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


# ===== ストーリー攻略 =====
def story():
    st.title(f"{st.session_state.starter} を選んだ人向け攻略")

    st.subheader("📖 ストーリーの進め方")
    st.write("""
    ・無理にレベルを上げなくてOK  
    ・タイプ相性だけ意識すれば大丈夫  
    ・負けてもペナルティはありません
    """)

    st.subheader("🗺️ おすすめレベル上げ場所")
    show_image("sv_map_all.png")

    if st.session_state.starter == "ニャオハ":
        st.write("草タイプが不利な炎ジムに注意！")
        st.write("おすすめ仲間：パモ、ウパー")

    elif st.session_state.starter == "ホゲータ":
        st.write("水タイプの敵には注意！")
        st.write("おすすめ仲間：マリル、シェルダー")

    elif st.session_state.starter == "クワッス":
        st.write("電気タイプに注意！")
        st.write("おすすめ仲間：ウパー、ディグダ")

    if st.button("最初に戻る"):
        st.session_state.page = "home"


# ===== 画面制御 =====
if st.session_state.page == "home":
    select_starter()
elif st.session_state.page == "story":
    story()


    # =========================
    # レベル別進行
    # =========================
    st.markdown("## 🗺 今おすすめの進行")

    if level <= 15:
        st.info("虫ジム → 岩ジム（無理せず）")
    elif level <= 25:
        st.info("草ジム → 水ジム")
    else:
        st.info("中盤以降のジム・スター団へ")

    # =========================
    # ジム注意
    # =========================
    st.markdown("## ⚠ ジムごとの注意点")

    if starter == "ニャオハ":
        st.warning("虫ジムは不利。仲間主体で戦おう。")
    elif starter == "ホゲータ":
        st.warning("水ジムは苦手。でんき・くさを連れていこう。")
    elif starter == "クワッス":
        st.warning("草ジムは厳しい。レベル上げが正解。")

    # =========================
    # メッセージ
    # =========================
    st.markdown("""
💡 **大事なこと**
- レベルを上げれば必ず進める  
- 逃げてもOK、それも戦略  
- 好きなポケモンを使っていい
""")

    if st.button("トップにもどる"):
        st.session_state.page = "home"

# =========================
# 画面切り替え
# =========================
if st.session_state.page == "starter":
    select_starter()
elif st.session_state.page == "home":
    home()
elif st.session_state.page == "story":
    story()


