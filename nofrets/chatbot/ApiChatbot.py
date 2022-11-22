from flask import Flask, request
from flask import jsonify
# import class chatbotservice
from ChatbotService import ChatbotService


# create an instance of the chatbot service
chatbot = ChatbotService()
app = Flask(__name__)

@app.route("/api/nofrets/sendmessage")
def sendMessage():
    content = request.json
    messageReturn = chatbot.sendMessage(content["sendMessage"])
    print(messageReturn)
    return jsonify ({
        'returnMessage': str(messageReturn),
        'sendMessage': content["sendMessage"]
        })