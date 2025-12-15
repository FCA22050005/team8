import streamlit as st

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
        st.image("images/sprigatito.png", width=120)
        if st.button("ニャオハ"):
            st.session_state.starter = "ニャオハ"
            st.session_state.page = "home"

    with col2:
        st.image("images/fuecoco.png", width=120)
        if st.button("ホゲータ"):
            st.session_state.starter = "ホゲータ"
            st.session_state.page = "home"

    with col3:
        st.image("images/quaxly.png", width=120)
        if st.button("クワッス"):
            st.session_state.starter = "クワッス"
            st.session_state.page = "home"


# =========================
# 御三家別トップ
# =========================
def home():
    st.title(f"{st.session_state.starter} を選んだあなたへ")

    st.info("""
この攻略は「失敗しない」ためのものではありません。
迷っても、遠回りしても、楽しめるように作っています。
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
    st.image("images/sv_map_all.png", use_container_width=True)

    level = st.slider("手持ちポケモンの平均レベル", 1, 60, 10)

    # -------------------------
    # 御三家別 基本アドバイス
    # -------------------------
    st.markdown("## あなたの御三家について")

    if starter == "ニャオハ":
        st.success("""
すばやくて動きやすいポケモンです。
ただし **ほのお・ひこう** が少し苦手です。
""")

    elif starter == "ホゲータ":
        st.success("""
バトルが安定しやすく初心者向けです。
**みずタイプ** には注意しましょう。
""")

    elif starter == "クワッス":
        st.success("""
序盤は少し大変ですが、必ず進めます。
**でんきタイプ** には注意しましょう。
""")

    # -------------------------
    # おすすめ仲間ポケモン
    # -------------------------
    st.markdown("## おすすめ仲間ポケモン")

    if starter == "ニャオハ":
        st.image("images/flying.png", width=100)
        st.markdown("""
**ひこうタイプ**
- ニャオハの苦手をカバー
- 旅で使いやすい
""")

    elif starter == "ホゲータ":
        st.image("images/water.png", width=100)
        st.markdown("""
**みずタイプ**
- ほのおの弱点をカバー
- 安定して戦える
""")

    elif starter == "クワッス":
        st.image("images/electric.png", width=100)
        st.markdown("""
**でんきタイプ**
- みずタイプと相性が良い
- ジム戦で安心
""")

    # -------------------------
    # ジムごとの注意点
    # -------------------------
    st.markdown("## ジム戦の注意ポイント")

    if starter == "ニャオハ":
        st.warning("""
- ほのおジム：無理に突っ込まない
- 仲間ポケモンを使えばOK
""")

    elif starter == "ホゲータ":
        st.warning("""
- みずジム：レベルを少し高めに
- でんき・くさの仲間がいると安心
""")

    elif starter == "クワッス":
        st.warning("""
- でんきジム：必ず仲間ポケモンを用意
- レベル上げで解決できる
""")

    # -------------------------
    # 心が折れないメッセージ
    # -------------------------
    st.markdown("""
💡 **大丈夫ポイント**
- レベルを上げれば必ず勝てます
- 苦手なら後回しでOK
- 好きなポケモンで進んで大丈夫
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
