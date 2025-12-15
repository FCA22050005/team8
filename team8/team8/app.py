import streamlit as st
from pathlib import Path

# =========================
# パス対策（Cloud対応）
# =========================
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"

def show_image(name, width=None):
    path = IMAGE_DIR / name
    if path.exists():
        st.image(str(path), width=width)
    else:
        st.error(f"画像が見つかりません: {path}")

# =========================
# 初期設定
# =========================
st.set_page_config(
    page_title="ポケモンSV 初心者サポート",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = "starter"

if "starter" not in st.session_state:
    st.session_state.starter = None


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

    st.markdown("### できること")
    st.markdown("""
- 御三家別おすすめ仲間ポケモン  
- ジムごとの注意ポイント  
- レベルに応じた無理のない進行
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

    # =========================
    # 御三家別おすすめ仲間
    # =========================
    st.markdown("## 🌟 おすすめ仲間ポケモン")

    if starter == "ニャオハ":
        st.success("""
- **パモ**：でんき技で飛行・水対策  
- **イワンコ**：タイプ相性に左右されにくい  
- **ドロバンコ**：耐久があり安定
""")

    elif starter == "ホゲータ":
        st.success("""
- **マリル**：みずタイプで弱点カバー  
- **パモ**：スピードとでんき技が便利  
- **ココガラ**：ひこうで安全に戦える
""")

    elif starter == "クワッス":
        st.success("""
- **パモ**：序盤の要  
- **ヤヤコマ**：ひこうで草・虫が楽  
- **イワンコ**：火力不足を補える
""")

    # =========================
    # レベル別進行ガイド
    # =========================
    st.markdown("## 🗺 今おすすめの進行")

    if level <= 15:
        st.info("虫ジム → 岩ジム（レベルを少し上げてから）")
    elif level <= 25:
        st.info("草ジム → 水ジム")
    else:
        st.info("中盤以降のジム・スター団へ")

    # =========================
    # ジム別注意点（御三家別）
    # =========================
    st.markdown("## ⚠ 御三家別 ジム注意点")

    if starter == "ニャオハ":
        st.warning("""
- **虫ジム**：タイプ不利。無理せず仲間に頼ろう  
- **炎ポケモンが出たら交代が正解**
""")

    elif starter == "ホゲータ":
        st.warning("""
- **水ジム**：弱点を突かれやすい  
- くさ・でんきタイプを連れて行こう
""")

    elif starter == "クワッス":
        st.warning("""
- **草ジム**：かなり不利  
- レベルを上げて仲間主体で戦おう
""")

    # =========================
    # 心が折れないためのメッセージ
    # =========================
    st.markdown("""
💡 **覚えておいてほしいこと**
- レベルを上げれば必ず進める  
- 逃げてもOK、別ルートも正解  
- 好きなポケモンを使っていい
""")

    if st.button("トップにもどる"):
        st.session_state.page = "home"


# =========================
# セーフティチェック
# =========================
if "page" not in st.session_state:
    st.session_state.page = "starter"

if "starter" not in st.session_state:
    st.session_state.starter = None

# starter が未選択なのに他ページに行こうとしたら戻す
if st.session_state.page != "starter" and st.session_state.starter is None:
    st.session_state.page = "starter"


# =========================
# 画面切り替え
# =========================
if st.session_state.page == "starter":
    select_starter()
elif st.session_state.page == "home":
    home()
elif st.session_state.page == "story":
    story()
