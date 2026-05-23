import streamlit as st
import random
import time
import os
import json  # 💾 ファイル保存のために追加

# 1. ページの設定
st.set_page_config(page_title="混沌のキメラ・ブリーダー", page_icon="🧬", layout="centered")

st.title("🧬 混沌のキメラ・ブリーダー")
st.caption("禁忌の錬金術で、世界に1体だけのハイブリッドモンスターを生み出せ！")

# 2. ベースとなる素材モンスターのデータ
BASE_MONSTERS = {
    "サンダーバード": {
        "hp": 100, "atk": 60, "spd": 90, "img_key": "bird", 
        "desc": "電撃を放つ怪鳥。すばやい。",
        "skills": ["ライトニングボルト", "高速移動"]
    },
    "マグロ": {
        "hp": 120, "atk": 30, "spd": 50, "img_key": "maguro", 
        "desc": "止まると死ぬ回遊魚。タフで新鮮。",
        "skills": ["アクアジェット", "不眠不休"]
    },
    "毒の茨": {
        "hp": 200, "atk": 65, "spd": 40, "img_key": "thorns", 
        "desc": "触れるもの全てを毒にする植物。攻撃力が高い。",
        "skills": ["ポイズンニードル", "光合成"]
    },
    "漆黒のドラゴン": {
        "hp": 250, "atk": 85, "spd": 70, "img_key": "dragon", 
        "desc": "全てを焼き尽くす闇の眷属。バランスが良い。",
        "skills": ["ダークネスブレス", "竜の威圧"]
    },
    "タコ": {
        "hp": 40, "atk": 20, "spd": 30, "img_key": "tako", 
        "desc": "ぬるぬるしている。足が8本ある。",
        "skills": ["スミ吐き", "再生触手"]
    },
}

# 💾 データのセーブ・ロード用関数
SAVE_FILE = "saved_chimeras.json"

def load_chimeras():
    """ファイルを読み込んでリストを返す。ファイルがない場合は空のリストを返す"""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_chimeras(chimera_list):
    """キメラのリストをファイルに保存する"""
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(chimera_list, f, ensure_ascii=False, indent=4)

# 3. セッション状態の初期化（セーブファイルからの読み込みに対応）
if "chimera_list" not in st.session_state:
    st.session_state.chimera_list = load_chimeras()  # 🔄 起動時に保存データをロード

if "current_chimera" not in st.session_state:
    st.session_state.current_chimera = None

# タブ機能
tab1, tab2 = st.tabs(["🧪 遺伝子融合研究室", "📖 混沌のキメラ図鑑"])

# ==========================================
# タブ1：遺伝子融合研究室（合成画面）
# ==========================================
with tab1:
    st.subheader("🧪 配合するベースを選択")

    col1, col2 = st.columns(2)

    with col1:
        parent_a = st.selectbox("親モンスターA", list(BASE_MONSTERS.keys()), index=0)
        img_a_path = f"images/{BASE_MONSTERS[parent_a]['img_key']}.png"
        if os.path.exists(img_a_path):
            st.image(img_a_path, use_container_width=True)
        else:
            st.write("🖼️ (画像準備中)")
        st.info(BASE_MONSTERS[parent_a]["desc"])
        st.caption(f"持ちスキル: {', '.join(BASE_MONSTERS[parent_a]['skills'])}")

    with col2:
        parent_b = st.selectbox("親モンスターB", list(BASE_MONSTERS.keys()), index=1)
        img_b_path = f"images/{BASE_MONSTERS[parent_b]['img_key']}.png"
        if os.path.exists(img_b_path):
            st.image(img_b_path, use_container_width=True)
        else:
            st.write("🖼️ (画像準備中)")
        st.info(BASE_MONSTERS[parent_b]["desc"])
        st.caption(f"持ちスキル: {', '.join(BASE_MONSTERS[parent_b]['skills'])}")

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
            c_name = f"【混沌】{name_a}{name_b}"
            
            data_a = BASE_MONSTERS[parent_a]
            data_b = BASE_MONSTERS[parent_b]
            c_hp = int((data_a["hp"] + data_b["hp"]) / 2 * random.uniform(0.8, 1.3))
            c_atk = int((data_a["atk"] + data_b["atk"]) / 2 * random.uniform(0.8, 1.3))
            c_spd = int((data_a["spd"] + data_b["spd"]) / 2 * random.uniform(0.8, 1.3))
            
            lines = [
                f"{parent_a}の特性と、{parent_b}の生態が奇跡の融合を果たした姿。",
                f"見た目は{parent_b}の面影を残すが、{parent_a}の恐ろしいオーラを放っている。",
                f"錬金術の禁忌が生み出した個体。内に秘めたパワーは計り知れない。"
            ]
            c_desc = random.choice(lines)
            
            skill_from_a = random.choice(data_a["skills"])
            skill_from_b = random.choice(data_b["skills"])
            c_skills = [skill_from_a, skill_from_b]
            
            keys = sorted([data_a["img_key"], data_b["img_key"]])
            c_img = f"images/{keys[0]}_{keys[1]}.png"
            
            new_chimera = {
                "name": c_name,
                "hp": c_hp,
                "atk": c_atk,
                "spd": c_spd,
                "desc": c_desc,
                "skills": c_skills,
                "img": c_img,
                "parents": f"{parent_a} × {parent_b}"
            }
            
            st.session_state.current_chimera = new_chimera
            st.session_state.chimera_list.append(new_chimera)
            
            # 💾 ファイルに即座に書き込んで保存
            save_chimeras(st.session_state.chimera_list)
            
            st.balloons()

    # 合成結果のリアルタイム表示
    if st.session_state.current_chimera:
        chimera = st.session_state.current_chimera
        st.write("---")
        st.header(f"👾 新種誕生：{chimera['name']}")
        
        if os.path.exists(chimera["img"]):
            st.image(chimera["img"], caption=chimera["name"], width=400)
        else:
            st.warning(f"⚠️ 画像ファイルが見つかりません: {chimera['img']}")
        
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("❤️ HP", chimera["hp"])
        m_col2.metric("⚔️ 攻撃力", chimera["atk"])
        m_col3.metric("⚡ すばやさ", chimera["spd"])
        
        st.markdown(f"**🧬 配合元:** {chimera['parents']}")
        st.markdown(f"**🔮 継承スキル:** `{', '.join(chimera['skills'])}`")
        st.markdown(f"> {chimera['desc']}")

# ==========================================
# タブ2：混沌のキメラ図鑑（一覧・閲覧画面）
# ==========================================
with tab2:
    st.subheader("📖 これまでに誕生したキメラ")
    
    if not st.session_state.chimera_list:
        st.info("まだキメラが登録されていません。研究室で合成を行ってください！")
    else:
        chimera_options = [f"{i+1}: {c['name']}" for i, c in enumerate(st.session_state.chimera_list)]
        selected_index = st.selectbox("閲覧するキメラを選択", range(len(chimera_options)), format_func=lambda x: chimera_options[x])
        selected_chimera = st.session_state.chimera_list[selected_index]
        
        st.write("---")
        st.subheader(selected_chimera["name"])
        
        v_col1, v_col2 = st.columns([1, 1])
        
        with v_col1:
            if os.path.exists(selected_chimera["img"]):
                st.image(selected_chimera["img"], use_container_width=True)
            else:
                st.write("🖼️ (画像準備中)")
                
        with v_col2:
            st.write(f"**❤️ HP:** {selected_chimera['hp']}")
            st.write(f"**⚔️ 攻撃力:** {selected_chimera['atk']}")
            st.write(f"**⚡ すばやさ:** {selected_chimera['spd']}")
            st.write(f"**🧬 配合元:** {selected_chimera['parents']}")
            st.write(f"**🔮 継承スキル:** `{', '.join(selected_chimera['skills'])}`")
            st.markdown(f"> {selected_chimera['desc']}")
        
        # ⚠️ 動画映え＆親切設計：図鑑リセットボタン（データを全消去したい時のため）
        st.write("---")
        if st.button("🗑️ 図鑑の記録をすべて抹消する", type="secondary"):
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
            st.session_state.chimera_list = []
            st.session_state.current_chimera = None
            st.rerun()