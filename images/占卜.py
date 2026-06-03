from datetime import datetime
import random
import time
import streamlit as st
import requests  # 👈 記得這個一定要導入，用來發射訊號給 n8n


# ==================== 核心邏輯 (保留你原本的寫法) ====================
class TarotCard:
    def __init__(self, name, meaning):
        self.name = name
        self.meaning = meaning
        self.is_upright = random.choice([True, False])

    def __str__(self):
        orientation = "【正位】" if self.is_upright else "【逆位】"
        return f"{self.name} {orientation}"


class TarotSystem:
    def __init__(self):
        raw_data = {
            "0 愚人": "自由、冒險、新的開始、潛能",
            "I 魔術師": "自信、創造力、意志力、行動",
            "II 女祭司": "智慧、直覺、神祕、潛意識",
            "III 皇后": "豐饒、愛、母性、感官享受",
            "IV 皇帝": "秩序、權力、穩定、理性",
            "V 教皇": "傳統、信仰、教育、規範",
            "VI 戀人": "選擇、結合、價值觀、愛情",
            "VII 戰車": "意志力、勝利、克服困難",
            "VIII 力量": "耐心、勇氣、內在控制、馴服",
            "IX 隱者": "內省、孤獨、尋找真理",
            "X 命運之輪": "命運、轉變、機會",
            "XI 正義": "公平、理性、因果、平衡",
            "XII 倒吊人": "犧牲、換位思考、暫停、領悟",
            "XIII 死神": "終結、蛻變、轉型",
            "XIV 節制": "平衡、中庸、調和",
            "XV 惡魔": "欲望、束縛、物質主義",
            "XVI 塔": "毀滅、突發事件、信念崩解",
            "XVII 星星": "希望、療癒、靈感",
            "XVIII 月亮": "迷惘、恐懼、潛意識、幻象",
            "XIX 太陽": "光明、成功、活力、喜悅",
            "XX 審判": "覺醒、重生、業力回報",
            "XXI 世界": "圓滿、整合、終點",
        }
        self.deck = [TarotCard(name, meaning) for name, meaning in raw_data.items()]

    def draw_spread(self, count=3):
        selected_cards = random.sample(self.deck, count)
        for card in selected_cards:
            card.is_upright = random.choice([True, False])
        return selected_cards

    def save_log(self, user_name, question, results):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("tarot_history.txt", "a", encoding="utf-8") as f:
            f.write(f"時間: {timestamp} | 使用者: {user_name}\n")
            f.write(f"問題: {question}\n")
            f.write(f"結果: {', '.join([str(card) for card in results])}\n")
            f.write("-" * 50 + "\n")


# ==================== Streamlit 網頁介面 ====================
if "system" not in st.session_state:
    st.session_state.system = TarotSystem()

st.set_page_config(page_title="小莫專業塔羅占卜", page_icon="🔮", layout="centered")
st.title("🔮 小莫專業塔羅占卜系統")
st.write("靜下心來，默想你的問題，讓神祕的塔羅牌帶給你啟示。")

# 側邊欄：使用者資訊
st.sidebar.header("👤 使用者設定")
user_name = st.sidebar.text_input("請輸入您的姓名：", value="訪客")

# 主畫面：輸入問題
question = st.text_input("💬 您想詢問什麼問題？", placeholder="例如：我近期的事業運勢如何？")

# 抽牌按鈕
# ==================== Streamlit 介面：抽牌與連線邏輯 ====================

# 增加一個控制狀態，記錄是否已經抽過牌
if "cards_drawn" not in st.session_state:
    st.session_state.cards_drawn = False
if "current_cards" not in st.session_state:
    st.session_state.current_cards = []

# 抽牌按鈕
if st.button("🌟 開始洗牌並感應能量", type="primary"):
    if not question:
        st.warning("請先輸入您想詢問的問題喔！")
    else:
        with st.spinner("正在洗牌並凝聚能量中... 請稍候..."):
            time.sleep(1.5)

        # 抽牌並記錄到 session_state 中，防止網頁刷新後牌卡消失
        st.session_state.current_cards = st.session_state.system.draw_spread(3)
        st.session_state.cards_drawn = True

        # 儲存紀錄到文字檔
        st.session_state.system.save_log(user_name, question, st.session_state.current_cards)

# 如果已經抽過牌，就秀出牌卡結果，並顯示「AI 解牌按鈕」
if st.session_state.cards_drawn:
    labels = ["【過去】", "【現在】", "【未來】"]
    st.success("✨ 占卜完成！以下是您的牌陣結果：")
    st.markdown("---")

    # 呈現三張牌
    cols = st.columns(3)
    for i, (label, card) in enumerate(zip(labels, st.session_state.current_cards)):
        with cols[i]:
            if card.is_upright:
                st.metric(label, f"🔴 {card.name} (正位)")
                st.info(f"**提示：發展順遂**\n\n關鍵字：{card.meaning}")
            else:
                st.metric(label, f"🔵 {card.name} (逆位)")
                st.error(f"**警示：能量受阻**\n\n留意點：{card.meaning}")

    st.caption("💾 占卜紀錄已成功同步寫入本機 `tarot_history.txt` 檔案中。")
    st.markdown("---")

    # 🔥 這裡就是第二步：獨立的 AI 解牌按鈕，點了絕對不會迷路！
    if st.button("🔮 召喚 Gemini 導師進行深度解牌", type="secondary"):
        with st.spinner("🔮 AI 占卜大師正在感應三張牌的時間流能量，撰寫深度報告中..."):

            # 1. 打包抽出來的三張牌
            cards = st.session_state.current_cards
            cards_summary = (
                f"過去：{str(cards[0])} (關鍵字: {cards[0].meaning}) | "
                f"現在：{str(cards[1])} (關鍵字: {cards[1].meaning}) | "
                f"未來：{str(cards[2])} (關鍵字: {cards[2].meaning})"
            )

            # 2. n8n 連線網址
            if "N8N_URL" in st.secrets:
                # 雲端環境：自動讀取 Streamlit 網頁後台設定的網路正式網址
                n8n_webhook_url = st.secrets["N8N_URL"]
            else:
                # 本機環境：如果找不到線上變數，就自動退回你本機電腦的網址
                n8n_webhook_url = "http://localhost:5678/webhook/babc16ae-3b59-4382-ad16-ff0232fe688f"

            # 3. 資料裝箱
            payload = {
                "name": user_name,
                "question": question,
                "card": cards_summary
            }

            try:
                # 4. 正式發送給 n8n
                # 加上這一行，告訴 ngrok 我們是自己人，直接放行
                headers = {"ngrok-skip-browser-warning": "true"}

                # 在 requests.post 裡面加上 headers=headers
                response = requests.post(n8n_webhook_url, json=payload, headers=headers)

                # 找到這一段並修改：
                if response.status_code == 200:
                    st.balloons()
                    st.subheader("🪐 Gemini 導師深度解牌報告")

                    # 這是最穩定的解析方式
                    try:
                        # 因為 n8n 回傳的是 JSON，我們要先抓出來
                        response_json = response.json()

                        # 根據我們之前的設定，文字內容會藏在這裡面
                        # 我們檢查一下不同的路徑，確保一定能抓到
                        report_text = response_json.get("text") or \
                                      response_json.get("output", {}).get("text") or \
                                      response.text

                        st.markdown(report_text)

                    except Exception as e:
                        # 如果解析 JSON 失敗，至少把原始文字顯示出來，讓你看到報告
                        st.markdown(response.text)
                else:
                    st.error(f"AI 導師目前有點忙碌 (錯誤碼: {response.status_code})，請稍後再試。")
            except Exception as e:
                st.error(
                    f"連線至 AI 發生錯誤: {e}\n\n💡 提示：請確認 n8n 的 Webhook 積木是否正維持在 'Listen for test event' 狀態喔！")