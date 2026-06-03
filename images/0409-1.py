import random
import time
from datetime import datetime


class TarotCard:
    """代表單張塔羅牌的類別"""

    def __init__(self, name, meaning):
        self.name = name
        self.meaning = meaning
        self.is_upright = random.choice([True, False])

    def __str__(self):
        orientation = "【正位】" if self.is_upright else "【逆位】"
        return f"{self.name} {orientation}"


class TarotSystem:
    """管理牌庫與抽牌邏輯的系統"""

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
            "XXI 世界": "圓滿、整合、終點"
        }
        self.deck = [TarotCard(name, meaning) for name, meaning in raw_data.items()]

    def draw_spread(self, count=3):
        """抽取不重複的牌陣並重新隨機決定正逆位"""
        # 為了讓每次抽牌的正逆位都隨機，我們在抽取時重新生成狀態
        selected_cards = random.sample(self.deck, count)
        for card in selected_cards:
            card.is_upright = random.choice([True, False])
        return selected_cards

    def save_log(self, user_name, question, results):
        """將抽牌結果存入文字檔，建立紀錄"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("tarot_history.txt", "a", encoding="utf-8") as f:
            f.write(f"時間: {timestamp} | 使用者: {user_name}\n")
            f.write(f"問題: {question}\n")
            f.write(f"結果: {', '.join([str(card) for card in results])}\n")
            f.write("-" * 50 + "\n")


def run_game():
    system = TarotSystem()
    print("🔮 小莫專業塔羅占卜系統 🔮")

    user_name = input("請輸入您的姓名：")

    # --- 加入迴圈 ---
    while True:
        print("\n" + "=" * 30)
        question = input("您想詢問什麼問題？ (輸入 'q' 離開系統): ")

        if question.lower() == 'q':
            print(f"\n感謝您的諮詢，{user_name}，祝您一切順心，再見！")
            break

        print("\n[系統] 正在洗牌並感應能量...")
        time.sleep(1.5)

        cards = system.draw_spread(3)
        labels = ["【過去】", "【現在】", "【未來】"]

        print("\n--- 占卜結果 ---")
        for label, card in zip(labels, cards):
            print(f"{label}: {card}")
            if not card.is_upright:
                print(f"   (警示：能量受阻或過度，請留意：{card.meaning})")
            else:
                print(f"   (提示：發展順遂，關鍵字：{card.meaning})")
            time.sleep(0.5)

        # 自動儲存紀錄
        system.save_log(user_name, question, cards)
        print("\n[系統] 占卜紀錄已存入 tarot_history.txt")

        # 詢問是否繼續
        cont = input("\n是否繼續下一次占卜？(y/n): ")
        if cont.lower() != 'y':
            print(f"\n感謝您的諮詢，{user_name}，再見！")
            break


if __name__ == "__main__":
    run_game()