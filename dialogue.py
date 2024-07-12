# dialogue.py
class DialogueManager:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "help": "You can ask me about the game or any other questions you have.",
            "quit": "Thank you for playing! See you next time."
        }

    def process_response(self, input_text):
        # Process the response logic here
        input_text = input_text.lower().strip()
        return self.responses.get(input_text, "I'm not sure how to respond to that.")
