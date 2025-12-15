import streamlit as st
from pathlib import Path

# =========================
# パス設定（画像は同階層）
# =========================
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR

def show_image(name, width=None):
    path = IMAGE_DIR / name
    if path.exists():
        st.image(str(path), width=width)
    else:
        st.warning(f"画像が見つかりません: {name}")

# =========================
# 初期設定
# =========================
st.set_page_config(
    page_title="ポケモンSV 初心者サポート",
    layout="centered"
)

# session_state 初期化
if "page" not in st.session_state:
    st.session_state.page = "starter"

if "starter" not in st.session_state:
    st.session_state.starter = None

# セーフティチェック（再読み込み対策）
if st.session_state.page != "starter" and st.session_state.starter is None:
    st.session_state.page = "starter"

# =========================
# 御三家選択画面
# =========================
def select_starter():
    st.title("最初に選んだポケモンを教えてください")
    st.markdown("### どれを選んでも大丈夫。あなたの選択を支えます。")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_image("sprigatito.png", width=120)
        if st.button("ニャオハ"):
            st.session_state.starter = "ニャオハ"
            st.session_state.page = "home"

    with col2:
        show_image("fuecoco.png", width=120)
        if st.button("ホゲータ"):
            st.session_state.starter = "ホゲータ"
            st.session_state.page = "home"

    with col3:
        show_image("quaxly.png", width=120)
        if st.button("クワッス"):
            st.session_state.starter = "クワッス"
            st.session_state.page = "home"

# =========================
# トップページ
# =========================
def home():
    starter = st.session_state.starter
    st.title(f"{starter} を選んだ人向け攻略")

    st.info("""
このサイトは「最短攻略」を目的としていません。
どの御三家でも、心が折れずに楽しめることを大切にしています。
""")

    if st.button("ストーリー攻略を見る"):
        st.session_state.page = "story"

    if st.button("御三家を選び直す"):
        st.session_state.page = "starter"

# =========================
# ストーリー攻略
# =========================
def story():
    starter = st.session_state.starter
    st.title("ストーリー攻略（初心者向け）")

    show_image("sv_map_all.png")

    level = st.slider("手持ちポケモンの平均レベル", 1, 60, 10)

    # おすすめ仲間
    st.markdown("## 🌟 御三家別おすすめ仲間")

    if starter == "ニャオハ":
        st.success("""
- パモ：でんきで弱点補助  
- イワンコ：安定アタッカー  
- ドロバンコ：耐久役
""")

    elif starter == "ホゲータ":
        st.success("""
- マリル：みずで弱点補助  
- パモ：スピード要員  
- ココガラ：安全枠
""")

    elif starter == "クワッス":
        st.success("""
- パモ：序盤の要  
- ヤヤコマ：ひこうで有利  
- イワンコ：火力補助
""")

    # レベル別進行
    st.markdown("## 🗺 今おすすめの進行")

    if level <= 15:
        st.info("虫ジム → 岩ジム（無理せず）")
    elif level <= 25:
        st.info("草ジム → 水ジム")
    else:
        st.info("中盤以降のジム・スター団へ")

    # ジム注意
    st.markdown("## ⚠ ジムごとの注意点")

    if starter == "ニャオハ":
        st.warning("虫ジムは不利。仲間主体で戦おう。")
    elif starter == "ホゲータ":
        st.warning("水ジムは苦手。でんき・くさを連れていこう。")
    elif starter == "クワッス":
        st.warning("草ジムは厳しい。レベル上げが正解。")

    # 心が折れないメッセージ
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
