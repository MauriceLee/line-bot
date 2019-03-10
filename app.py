from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('MM9ROyV1RXUkOBKNMu7NgRbPJM07/g2oQ6taWg4fw5FMzqy5t23JkUHVmesdCiwmF5Ff0I3mmqKao/qnEkLZkkep/JTakWq7j2op3lb5Y9V+sp8Plb1545Y5/53LKHukkeuenai9Jps8KJnWyxPkzwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1c59d31f39a3d23abb86f17628625c90')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '你吃飯了嗎'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()