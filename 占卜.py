import random
import streamlit as st
import requests
import time

# ==================== CSS 特效 ====================
st.markdown("""
<style>
@keyframes sparkle {
  0%, 100% { opacity: 0; transform: scale(0.5); }
  50% { opacity: 1; transform: scale(1); }
}
.sparkle {
  color: #FFD700;
  font-size: 1.2rem;
  font-weight: bold;
  animation: sparkle 2s infinite ease-in-out;
  text-align: center;
  padding: 10px;
}
</style>
""", unsafe_allow_html=True)


# ==================== 核心邏輯 ====================
class TarotCard:
    def __init__(self, name, meaning):
        self.name = name
        self.meaning = meaning
        self.is_upright = random.choice([True, False])


class TarotSystem:
    def __init__(self):
        raw_data = {
            "0 愚人": "自由、冒險、新的開始", "I 魔術師": "自信、創造力、意志力", "II 女祭司": "智慧、直覺、神祕",
            "III 皇后": "豐饒、愛、感官享受", "IV 皇帝": "秩序、權力、穩定", "V 教皇": "傳統、信仰、規範",
            "VI 戀人": "選擇、結合、價值觀", "VII 戰車": "意志力、勝利、克服困難", "VIII 力量": "耐心、勇氣、內在控制",
            "IX 隱者": "內省、孤獨、尋找真理", "X 命運之輪": "命運、轉變、機會", "XI 正義": "公平、理性、平衡",
            "XII 倒吊人": "犧牲、換位思考、暫停", "XIII 死神": "終結、蛻變、轉型", "XIV 節制": "平衡、中庸、調和",
            "XV 惡魔": "欲望、束縛、物質主義", "XVI 塔": "毀滅、突發事件、信念崩解", "XVII 星星": "希望、療癒、靈感",
            "XVIII 月亮": "迷惘、恐懼、幻象", "XIX 太陽": "光明、成功、活力", "XX 審判": "覺醒、重生、業力回報",
            "XXI 世界": "圓滿、整合、終點",
            "權杖一": "新機會", "權杖二": "規劃", "權杖三": "擴展", "權杖四": "慶祝", "權杖五": "競爭",
            "權杖六": "成功", "權杖七": "防禦", "權杖八": "快速移動", "權杖九": "堅持", "權杖十": "重擔",
            "權杖侍者": "熱情", "權杖騎士": "行動", "權杖皇后": "活力", "權杖國王": "領袖",
            "聖杯一": "情感啟動", "聖杯二": "連結", "聖杯三": "友誼", "聖杯四": "冷漠", "聖杯五": "遺憾",
            "聖杯六": "懷舊", "聖杯七": "選擇", "聖杯八": "放棄", "聖杯九": "滿足", "聖杯十": "幸福",
            "聖杯侍者": "情感消息", "聖杯騎士": "浪漫", "聖杯皇后": "直覺", "聖杯國王": "慈悲",
            "寶劍一": "清晰", "寶劍二": "僵局", "寶劍三": "心碎", "寶劍四": "休息", "寶劍五": "失敗",
            "寶劍六": "平靜遷移", "寶劍七": "策略", "寶劍八": "受限", "寶劍九": "焦慮", "寶劍十": "終結",
            "寶劍侍者": "警覺", "寶劍騎士": "衝動", "寶劍皇后": "獨立", "寶劍國王": "權威",
            "金幣一": "顯化", "金幣二": "平衡", "金幣三": "合作", "金幣四": "節儉", "金幣五": "匱乏",
            "金幣六": "給予", "金幣七": "評估", "金幣八": "勤奮", "金幣九": "自足", "金幣十": "傳承",
            "金幣侍者": "學習", "金幣騎士": "穩定", "金幣皇后": "富足", "金幣國王": "富裕"
        }
        self.deck = [TarotCard(name, meaning) for name, meaning in raw_data.items()]

    def draw_spread(self, count):
        return random.sample(self.deck, count)


# ==================== Streamlit 介面 ====================
if "system" not in st.session_state: st.session_state.system = TarotSystem()

st.set_page_config(page_title="小莫不專業塔羅系統", page_icon="🔮")
st.title("🔮 小莫不專業塔羅系統")

user_name = st.sidebar.text_input("👤 您的姓名：", value="訪客")
option = st.sidebar.selectbox("選擇牌陣：", ["單張靈感", "過去現在未來", "深度探索"])
count = {"單張靈感": 1, "過去現在未來": 3, "深度探索": 5}[option]
question = st.text_input("💬 想詢問的問題：")

if st.button("🌟 開始洗牌"):
    if question:
        with st.spinner("正在為你洗牌，連結宇宙能量中..."):
            time.sleep(1.5)
            st.session_state.current_cards = st.session_state.system.draw_spread(count)
            st.session_state.cards_drawn = True
            st.rerun()
    else:
        st.warning("請先輸入問題喔！")

if st.session_state.get("cards_drawn"):
    # 使用 CSS 來優化卡片外觀
    st.markdown("""
    <style>
    .tarot-card {
        background-color: #1e2530;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 20px 10px;
        text-align: center;
        height: 320px; /* 固定高度，讓所有卡片對齊 */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .emoji-size { font-size: 3rem; margin-bottom: 10px; }
    .card-name { font-size: 1.1rem; font-weight: bold; margin-bottom: 5px; }
    .card-meaning { font-size: 0.85rem; color: #bbb; line-height: 1.4; }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(count)
    element_icons = {
        "權杖": "🔥", "聖杯": "💧", "寶劍": "⚔️", "金幣": "💰", "愚人": "🃏", "魔術師": "🪄", "女祭司": "📜",
        "皇后": "👑", "皇帝": "🏛️", "教皇": "⛪", "戀人": "❤️", "戰車": "🐎", "力量": "🦁", "隱者": "🕯️",
        "命運": "🎡", "正義": "⚖️", "倒吊人": "🧘", "死神": "💀", "節制": "🏺", "惡魔": "⛓️", "塔": "⚡",
        "星星": "🌟", "月亮": "🌙", "太陽": "☀️", "審判": "🎺", "世界": "🌍"
    }

    for i, card in enumerate(st.session_state.current_cards):
        with cols[i]:
            time.sleep(0.3)
            icon = next((icon for key, icon in element_icons.items() if key in card.name), "🎴")
            orientation = "【正位】" if card.is_upright else "【逆位】"

            # 使用 HTML/CSS 建立精緻卡片
            st.markdown(f"""
            <div class="tarot-card">
                <div class="emoji-size">{icon}</div>
                <div class="card-name">{card.name}</div>
                <div style="color: #66ccff; font-size: 0.9rem;">{orientation}</div>
                <hr style="margin: 10px 0; border: 0.5px solid #444;">
                <div class="card-meaning">{card.meaning}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🔮 召喚小莫深度解牌"):
        st.markdown('<div class="sparkle">✨ 星光閃爍，能量凝聚中... ✨</div>', unsafe_allow_html=True)

        n8n_webhook_url = "https://wrecking-outlook-lesser.ngrok-free.dev/webhook/babc16ae-3b59-4382-ad16-ff0232fe688f"
        payload = {
            "name": user_name,
            "question": question,
            "card": str([(c.name + ("【正位】" if c.is_upright else "【逆位】")) for c in st.session_state.current_cards])
        }

        try:
            response = requests.post(n8n_webhook_url, json=payload, timeout=60)

            if response.status_code == 200:
                # 這裡我們不直接用 response.json()，因為它對特殊字元很敏感
                # 我們先把內容轉成文字，並過濾掉那些會造成崩潰的非法字元
                raw_text = response.text

                # 簡單修正常見的 JSON 衝突：把不合法的換行轉義
                clean_text = raw_text.replace('\n', '\\n').replace('\r', '\\r')

                # 嘗試解析
                import json

                data = json.loads(clean_text)

                st.subheader("🪐  小莫導師深度報告")
                ai_text = data.get('output', '小莫導師剛剛靈感閃現，但沒說出話來...')
                st.markdown(ai_text)
            else:
                st.error(f"伺服器回應異常，狀態碼: {response.status_code}")

        except Exception as e:
            st.error(f"系統發生了一點小插曲: {e}")
            st.caption("建議檢查 n8n 的輸出，確認 AI 生成的內容沒有奇怪的隱藏符號。")
