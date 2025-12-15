import streamlit as st
from pathlib import Path
from PIL import Image

# ======================
# 基本設定
# ======================
BASE_DIR = Path(__file__).parent

if "page" not in st.session_state:
    st.session_state.page = "home"

if "starter" not in st.session_state:
    st.session_state.starter = None


# ======================
# 画像表示
# ======================
def show_image(filename):
    path = BASE_DIR / filename
    image = Image.open(path)
    st.image(image, use_column_width=True)


# ======================
# 御三家選択
# ======================
def home():
    st.title("ポケモンSV｜初心者限定攻略サイト")
    st.write("どの御三家を選んでも、必ずクリアできます。")

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


# ======================
# 攻略画面
# ======================
def story():
    starter = st.session_state.starter
    st.title(f"{starter} を選んだ人向け攻略")

    st.markdown("""
### 🎮 このサイトの考え方
- レベルを上げれば必ず勝てる  
- 負けてもペナルティなし  
- 好きなポケモンを使ってOK  
""")

    # ======================
    # 手持ちポケモン入力
    # ======================
    st.subheader("🎒 手持ちポケモンのレベル")

    levels = []
    cols = st.columns(6)

    for i in range(6):
        with cols[i]:
            lv = st.number_input(
                f"{i+1}匹目",
                min_value=1,
                max_value=100,
                value=1,
                key=f"poke{i}"
            )
            levels.append(lv)

    avg_level = sum(levels) / len(levels)
    st.success(f"平均レベル：{avg_level:.1f}")

    # ======================
    # マップ
    # ======================
    st.subheader("🗺 マップ全体")
    show_image("sv_map_all.png")

    # ======================
    # ジム・イベントデータ
    # ======================
    gyms = {
        "むしジム": {"lv": 15, "danger": "ほのお・ひこうが有利"},
        "いわヌシ": {"lv": 16, "danger": "くさ・みずでOK"},
        "くさジム": {"lv": 17, "danger": "ほのおが有利"},
        "ひこうヌシ": {"lv": 19, "danger": "でんきが有利"},
        "あくスター団": {"lv": 21, "danger": "かくとうが有利"},
        "でんきジム": {"lv": 24, "danger": "じめんが有利"},
        "ほのおスター団": {"lv": 27, "danger": "みずが安定"},
        "はがねヌシ": {"lv": 28, "danger": "ほのお・じめん"},
        "みずジム": {"lv": 30, "danger": "でんき・くさ"},
        "どくスター団": {"lv": 33, "danger": "じめん"},
        "ノーマルジム": {"lv": 36, "danger": "かくとう"},
        "ゴーストジム": {"lv": 42, "danger": "あく・ゴースト"},
        "エスパージム": {"lv": 45, "danger": "あく"},
        "こおりジム": {"lv": 48, "danger": "ほのお"},
        "フェアリースター団": {"lv": 51, "danger": "はがね"},
        "ドラゴンヌシ": {"lv": 55, "danger": "フェアリー"},
        "かくとうスター団": {"lv": 56, "danger": "ひこう・エスパー"},
    }

    # ======================
    # ジム選択
    # ======================
    st.subheader("🏟 ジム・イベントを選ぶ")

    gym_name = st.selectbox("行きたい場所を選んでください", gyms.keys())
    gym = gyms[gym_name]

    st.markdown(f"""
### 📍 {gym_name}
- 推奨レベル：Lv.{gym["lv"]}
- 有利タイプ：{gym["danger"]}
""")

    # ======================
    # レベル判定
    # ======================
    if avg_level >= gym["lv"]:
        st.success("今のレベルで挑戦できます！")
    else:
        st.warning("レベルが足りません。先にレベル上げをしましょう。")

        st.markdown("""
### 🐾 おすすめレベル上げ
- 周辺の草原エリアで野生ポケモン狩り
- テラスタルポケモンに挑戦
- レイドバトル（★1〜2）
""")

    # ======================
    # 御三家別注意
    # ======================
    st.subheader("⚠ 御三家別ワンポイント")

    if starter == "ニャオハ":
        st.write("🔥 炎・虫相手は無理しない")
    elif starter == "ホゲータ":
        st.write("💧 水タイプは仲間で対処")
    elif starter == "クワッス":
        st.write("⚡ 電気タイプは要注意")

    if st.button("御三家選択に戻る"):
        st.session_state.page = "home"


# ======================
# 画面制御
# ======================
if st.session_state.page == "home":
    home()
elif st.session_state.page == "story":
    story()
