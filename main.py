from flask import Flask, render_template, request, jsonify
import os
import jieba
import sys
from TalkBot import TalkBot
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
bot = bot = TalkBot();

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    res = bot.respond(message)
    return jsonify({'status': 'OK', 'answer': res})

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
