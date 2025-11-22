from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8154181736:AAGppPLQKMrf-iLZ1DQxjwq9LBnb4LGavz8"
CHAT_ID = "545134584"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

@app.route("/alert", methods=["GET", "POST"])
def alert():
    message = request.args.get("msg") or request.form.get("msg")

    if not message:
        return "No message received", 400

    print(f"Alert received: {message}")
    send_telegram(message)

    return "Alert sent to Telegram", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
