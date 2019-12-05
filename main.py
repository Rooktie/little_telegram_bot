# coding: utf-8

from flask import Flask, request, jsonify
from flask_sslify import SSLify
import config
import requests
import json
import bash_random_parser
import random_pick_taker
import news_parser

URL = "https://api.telegram.org/bot" + config.token + "/"
# setWebhook
# https://api.telegram.org/bot262770011:AAFqvM20Pm34Q5jXsZeMuodLgTGYoLuKRxU/setWebhook?url=/262770011:AAFqvM20Pm34Q5jXsZeMuodLgTGYoLuKRxU
app = Flask(__name__)
sslify = SSLify(app)


def send_message(chat_id, text="bla-bla-bla"):
    url = URL + "sendMessage"
    answer = {"chat_id": chat_id, "text": text}
    r = requests.post(url, json=answer)
    return r.json()


@app.route("/262770011:AAFqvM20Pm34Q5jXsZeMuodLgTGYoLuKRxU", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        r = request.get_json()
        chat_id = r["message"]["chat"]["id"]
        message = r["message"]["text"]
        try:
            command = r["message"]["entities"][-1]["type"]
            if command == "bot_command":
                if message == "/joke":
                    send_message(chat_id, bash_random_parser.end_text())
                elif message == "/image":
                    send_message(chat_id, random_pick_taker.generate_image_link())
                elif message == "/news":
                    send_message(chat_id, news_parser.tell_news())
        except:
            text = "есть три команды /joke, /image и /news что бы что-то получить вам нужно их ввести"
            send_message(chat_id, text)
    return "<h1>hello username</h1>"


if __name__ == "__main__":
    app.run()
