import streamlit as st
import random
import time
import os
import json

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
    "九尾の狐": {
        "hp": 150, "atk": 70, "spd": 80, "img_key": "fox", 
        "desc": "神秘的な力を持つ妖狐。素早くて攻撃的。",
        "skills": ["狐火", "幻術の舞"]
    },
    "古代の聖女": {
        "hp": 180, "atk": 50, "spd": 60, "img_key": "rumi", 
        "desc": "癒しの力を持つ聖女。防御力が高い。",
        "skills": ["ヒーリングライト", "聖なる盾"]
    },
    "近未来の攻撃ドローン": {
        "hp": 80, "atk": 90, "spd": 100, "img_key": "drone", 
        "desc": "最新鋭の攻撃ドローン。攻撃力とすばやさが抜群。",
        "skills": ["ミサイルランチャー", "ステルスモード"]
    },
    "風の剣士": {
        "hp": 130, "atk": 75, "spd": 85, "img_key": "wind", 
        "desc": "風を操る剣士。バランスの取れたステータス。",
        "skills": ["エアスラッシュ", "風の加護"]
    },
}

# 💾 データのセーブ・ロード用関数
SAVE_FILE = "saved_chimeras.json"

def load_chimeras():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_chimeras(chimera_list):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(chimera_list, f, ensure_ascii=False, indent=4)

# 3. セッション状態の初期化
if "chimera_list" not in st.session_state:
    st.session_state.chimera_list = load_chimeras()

if "current_chimera" not in st.session_state:
    st.session_state.current_chimera = None

# ✨ 3つのタブに拡張（闘技場を追加）
tab1, tab2, tab3 = st.tabs(["🧪 遺伝子融合研究室", "📖 混沌のキメラ図鑑", "⚔️ 混沌の闘技場"])

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
            progress_text = "遺伝子を分解中..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                if percent_complete == 40:
                    my_bar.progress(percent_complete, text="細胞を強制結合しています...")
                elif percent_complete == 80:
                    my_bar.progress(percent_complete, text="魂の定着を確認...")
            my_bar.empty()

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
            save_chimeras(st.session_state.chimera_list)
            st.balloons()

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
        selected_index = st.selectbox("閲覧するキメラを選択", range(len(chimera_options)), format_func=lambda x: chimera_options[x], key="view_select")
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
        
        st.write("---")
        if st.button("🗑️ 図鑑の記録をすべて抹消する", type="secondary"):
            if os.path.exists(SAVE_FILE):
                os.remove(SAVE_FILE)
            st.session_state.chimera_list = []
            st.session_state.current_chimera = None
            st.rerun()

# ==========================================
# ⚔️ タブ3：混沌の闘技場（自動戦闘シミュレーション機能）
# ==========================================
with tab3:
    st.subheader("⚔️ キメラコロシアム")
    
    if len(st.session_state.chimera_list) < 2:
        st.warning("バトルを始めるには、図鑑に最低2体以上のキメラが必要です！もっと合成して仲間を増やしましょう。")
    else:
        st.write("対戦させる2体のキメラを選択してください。")
        
        b_col1, b_col2 = st.columns(2)
        chimera_options = [f"{i+1}: {c['name']}" for i, c in enumerate(st.session_state.chimera_list)]
        
        with b_col1:
            p1_idx = st.selectbox("🔴 プレイヤー1 (先攻側)", range(len(chimera_options)), format_func=lambda x: chimera_options[x], index=0)
            p1 = st.session_state.chimera_list[p1_idx]
            if os.path.exists(p1["img"]):
                st.image(p1["img"], use_container_width=True)
            st.caption(f"❤️HP:{p1['hp']} ⚔️ATK:{p1['atk']} ⚡SPD:{p1['spd']}")

        with b_col2:
            # 被りを防ぐためデフォルトの初期位置をズラす（2体以上いる場合）
            default_p2 = 1 if len(chimera_options) > 1 else 0
            p2_idx = st.selectbox("🔵 プレイヤー2 (後攻側)", range(len(chimera_options)), format_func=lambda x: chimera_options[x], index=default_p2)
            p2 = st.session_state.chimera_list[p2_idx]
            if os.path.exists(p2["img"]):
                st.image(p2["img"], use_container_width=True)
            st.caption(f"❤️HP:{p2['hp']} ⚔️ATK:{p2['atk']} ⚡SPD:{p2['spd']}")

        st.write("---")
        
        # 💥 バトル開始ボタン
        if st.button("⚔️ デスマッチ、戦闘開始！！ ⚔️", use_container_width=True, type="primary"):
            st.subheader("🎬 ライブ戦闘ログ")
            
            # バトル用の一時ステータス（HP）をセット
            hp1, hp2 = p1["hp"], p2["hp"]
            
            # プレースホルダー（文字がリアルタイムに追記されていく領域）を作成
            log_placeholder = st.empty()
            battle_log = f"### ⚔️ {p1['name']} VS {p2['name']} ⚔️\n\n"
            log_placeholder.markdown(battle_log)
            time.sleep(1.0)
            
            # 先制判定（すばやさが高い方がファーストアタッカー）
            if p1["spd"] >= p2["spd"]:
                attacker, defender = p1, p2
                att_hp, def_hp = hp1, hp2
                p1_turn = True
            else:
                attacker, defender = p2, p1
                att_hp, def_hp = hp2, hp1
                p1_turn = False
                
            battle_log += f"⚡ すばやさ判定：**{attacker['name']}** が先手を取った！\n\n---\n"
            log_placeholder.markdown(battle_log)
            time.sleep(1.0)

            # 戦闘メインループ（最大20ターン）
            turn = 1
            while att_hp > 0 and def_hp > 0 and turn <= 20:
                battle_log += f"**【ターン {turn}】**\n"
                
                # 🎲 スキル発動判定（35%の確率で継承スキルが炸裂）
                if random.random() < 0.35:
                    activated_skill = random.choice(attacker["skills"])
                    damage = int(attacker["atk"] * random.uniform(1.3, 1.8))  # スキルは1.3〜1.8倍ダメ
                    battle_log += f"🌟 {attacker['name']}のスキル **『{activated_skill}』** が発動！！\n"
                else:
                    # 通常攻撃
                    damage = int(attacker["atk"] * random.uniform(0.8, 1.2))
                    
                def_hp -= damage
                if def_hp < 0:
                    def_hp = 0
                    
                battle_log += f"💥 {attacker['name']} の攻撃！ {defender['name']} に **{damage}** のダメージ！\n"
                battle_log += f"🍏 {defender['name']} の残りHP: **{def_hp}**\n\n"
                
                log_placeholder.markdown(battle_log)
                time.sleep(1.2)  # 🎬 動画映えポイント：絶妙なウェイトを入れる
                
                # 攻守交替
                if def_hp <= 0:
                    break
                
                attacker, defender = defender, attacker
                att_hp, def_hp = def_hp, att_hp
                p1_turn = not p1_turn
                turn += 1

            # 🏁 決着
            battle_log += "---\n### 🏆 試合終了 🏆\n"
            if def_hp <= 0:
                battle_log += f"🎉 勝者：**{attacker['name']}** の圧倒的勝利！！\n"
            else:
                battle_log += "⏳ 20ターンが経過した…！ 引き分け！\n"
                
            log_placeholder.markdown(battle_log)