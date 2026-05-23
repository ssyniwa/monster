import streamlit as st
import random
import time
import os

# 1. ページの設定
st.set_page_config(page_title="混沌のキメラ・ブリーダー", page_icon="🧬", layout="centered")

st.title("🧬 混沌のキメラ・ブリーダー")
st.caption("禁忌の錬金術で、世界に1体だけのハイブリッドモンスターを生み出せ！")

# 2. ベースとなる素材モンスターのデータ（img_key を追加）
BASE_MONSTERS = {
    "サンダーバード": {"hp": 100, "atk": 60, "spd": 90, "img_key": "bird", "desc": "電撃を放つ怪鳥。すばやい。"},
    "マグロ": {"hp": 120, "atk": 30, "spd": 50, "img_key": "maguro", "desc": "止まると死ぬ回遊魚。タフで新鮮。"},
    "毒の茨": {"hp": 200, "atk": 65, "spd": 40, "img_key": "thorns", "desc": "触れるもの全てを毒にする植物。攻撃力が高い。"},
    "漆黒のドラゴン": {"hp": 250, "atk": 85, "spd": 70, "img_key": "dragon", "desc": "全てを焼き尽くす闇の眷属。バランスが良い。"},
    "タコ": {"hp": 40, "atk": 20, "spd": 30, "img_key": "tako", "desc": "ぬるぬるしている。足が8本ある。"},
}

# 3. セッション状態の初期化
if "chimera_created" not in st.session_state:
    st.session_state.chimera_created = False
    st.session_state.c_name = ""
    st.session_state.c_hp = 0
    st.session_state.c_atk = 0
    st.session_state.c_spd = 0
    st.session_state.c_desc = ""
    st.session_state.c_img = "" # キメラ画像パス用

# 4. UI配置：親モンスターの選択画面
st.subheader("🧪 配合するベースを選択")

col1, col2 = st.columns(2)

with col1:
    parent_a = st.selectbox("親モンスターA", list(BASE_MONSTERS.keys()), index=0)
    # 🖼️ 親Aの画像を表示
    img_a_path = f"images/{BASE_MONSTERS[parent_a]['img_key']}.png"
    if os.path.exists(img_a_path):
        st.image(img_a_path, use_container_width=True)
    else:
        st.write("🖼️ (画像準備中)")
    st.info(BASE_MONSTERS[parent_a]["desc"])

with col2:
    parent_b = st.selectbox("親モンスターB", list(BASE_MONSTERS.keys()), index=1)
    # 🖼️ 親Bの画像を表示
    img_b_path = f"images/{BASE_MONSTERS[parent_b]['img_key']}.png"
    if os.path.exists(img_b_path):
        st.image(img_b_path, use_container_width=True)
    else:
        st.write("🖼️ (画像準備中)")
    st.info(BASE_MONSTERS[parent_b]["desc"])

# 5. 禁断の合成ボタンと演出
st.write("---")
if st.button("🔥 禁忌のキメラ合成を実行する 🔥", use_container_width=True):
    if parent_a == parent_b:
        st.warning("同じモンスター同士では、混沌のエネルギーが拒絶反応を起こします！別の種類を選んでください。")
    else:
        # 🎬 カウントダウン演出
        progress_text = "遺伝子を分解中..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            if percent_complete == 40:
                my_bar.progress(percent_complete, text="細胞を強制結合しています...")
            elif percent_complete == 80:
                my_bar.progress(percent_complete, text="魂の定着を確認...")
        my_bar.empty()

        # 🧠 合成ロジック
        name_a = parent_a[:3]
        name_b = parent_b[-3:]
        st.session_state.c_name = f"【混沌】{name_a}{name_b}"
        
        data_a = BASE_MONSTERS[parent_a]
        data_b = BASE_MONSTERS[parent_b]
        st.session_state.c_hp = int((data_a["hp"] + data_b["hp"]) / 2 * random.uniform(0.8, 1.3))
        st.session_state.c_atk = int((data_a["atk"] + data_b["atk"]) / 2 * random.uniform(0.8, 1.3))
        st.session_state.c_spd = int((data_a["spd"] + data_b["spd"]) / 2 * random.uniform(0.8, 1.3))
        
        lines = [
            f"{parent_a}の凶暴性と、{parent_b}の奇妙な生態が奇跡の融合を果たした姿。",
            f"見た目はほぼ{parent_b}だが、{parent_a}のような恐ろしいオーラを放っている。",
            f"錬金術の失敗作に見えるが、内に秘めたパワーは計り知れない。"
        ]
        st.session_state.c_desc = random.choice(lines)
        
        # 🖼️ 合成結果の画像パスを決定 (例: mouse_maguro.png)
        # どちらをAに選んでも同じ画像になるようにアルファベット順でソートして結合する工夫
        keys = sorted([data_a["img_key"], data_b["img_key"]])
        st.session_state.c_img = f"images/{keys[0]}_{keys[1]}.png"
        
        st.session_state.chimera_created = True

# 6. 合成結果の表示
if st.session_state.chimera_created:
    st.balloons()
    
    st.header(f"👾 誕生：{st.session_state.c_name}")
    
    # 🎬 動画映え最大ポイント：完成したキメラ画像をドカンと真ん中に表示
    if os.path.exists(st.session_state.c_img):
        st.image(st.session_state.c_img, caption=st.session_state.c_name, width=400)
    else:
        st.warning(f"⚠️ 画像ファイルが見つかりません: {st.session_state.c_img}")
    
    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("❤️ HP", st.session_state.c_hp)
    m_col2.metric("⚔️ 攻撃力", st.session_state.c_atk)
    m_col3.metric("⚡ すばやさ", st.session_state.c_spd)
    
    st.blockquote(st.session_state.c_desc)