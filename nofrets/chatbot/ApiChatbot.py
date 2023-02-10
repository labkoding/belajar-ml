from flask import Flask, request
from flask import jsonify
# import class chatbotservice
from ChatbotService import ChatbotService


# create an instance of the chatbot service
chatbot = ChatbotService()
app = Flask(__name__)

@app.route("/api/nofretst/sendmessage")
def sendMessage():
    content = request.json
    messageReturn = chatbot.sendMessage(content["sendMessage"])
    print(messageReturn)
    return jsonify ({
        'returnMessage': str(messageReturn),
        'sendMessage': content["sendMessage"]
        })
@app.route("/api/nofrets/receivemessage", methods=['GET', 'POST'])
def receiveMessage():
    content = request.json
    if content is not None:
        print(content)
    # res.send(req.query['hub.challenge']);
    # user = request.args.get('user')
    # return jsonify ({
    #     'status': 'OK'
    #     })
    # return request.args.get('hub.challenge')
    return "ok"