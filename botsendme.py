"""Bot send me."""

from flask import Flask, abort, request, jsonify
import requests

import settings

app = Flask(__name__)


def sendmessage(message):
    """Send message."""
    tg = "https://api.telegram.org/bot" + settings.token
    data = {
        "chat_id": settings.chat_id,
        "text": message
        # "disable_web_page_preview": "true",
        # "disable_notification": True,
        # "parse_mode": "HTML"
    }
    requests.post(tg + "/sendMessage", json=data)


@app.route('/', methods=['GET', 'POST'])
def botsendme():
    """Bot send me."""
    if request.method == 'GET':
        try:
            sendmessage(request.args['message'])
        except Exception:
            abort(400)
    else:
        try:
            sendmessage(request.get_json()['message'])
        except Exception:
            abort(400)
    return jsonify({"message": "message sent"})


if __name__ == '__main__':
    app.run()

