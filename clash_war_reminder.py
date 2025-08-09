import requests
import time
import os

# ==== Налаштування через змінні оточення ====
CLAN_TAG = "G2VC2LRG"  # тег клану без #
CR_API_TOKEN = os.getenv("CR_API_TOKEN")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Відповідність: тег гравця -> Telegram ID
PLAYER_CONTACTS = {
    "#PLAYER_TAG1": 123456789,  # приклад
    "#PLAYER_TAG2": 987654321,
}

def get_clan_members():
    url = f"https://api.clashroyale.com/v1/clans/%23{CLAN_TAG}"
    headers = {"Authorization": f"Bearer {CR_API_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    return data.get("memberList", [])

def send_telegram_message(user_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": user_id, "text": text}
    requests.post(url, data=payload)

def main():
    while True:
        members = get_clan_members()
        for m in members:
            tag = m["tag"]
            name = m["name"]

            # TODO: Додати реальну перевірку боїв у війні
            if tag in PLAYER_CONTACTS:
                send_telegram_message(
                    PLAYER_CONTACTS[tag],
                    f"⚠️ {name}, не забудь відіграти кв у Clash Royale!"
                )
                time.sleep(1)

        print("✅ Перевірка завершена. Чекаю 1 годину...")
        time.sleep(3600)  # перевіряти щогодини

if __name__ == "__main__":
    main()
