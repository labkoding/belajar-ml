from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class ChatbotService:
    def __init__(self):
        self.chatbot = ChatBot('Charlie')
        trainer = ListTrainer(self.chatbot)
        trainer.train([
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ])
    def sendMessage(self, message):
        response = self.chatbot.get_response(message)
        return response