from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def sendMessage(message):
    # Create a new chat bot named Charlie
    chatbot = ChatBot('Charlie')
    trainer = ListTrainer(chatbot)
    trainer.train([
        "hello, good morning",
        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked.",
        'Hello',
        'Hi there!',
        'How are you doing?',
        'I\'m doing great.',
        'That is good to hear',
        'Thank you.',
        'You\'re welcome.',
    ])
    response = chatbot.get_response('hello')
    return response

# Get a response to the input text 'I would like to book a flight.'
# response = chatbot.get_response('I would like to book a flight.')
print(sendMessage('hi'))