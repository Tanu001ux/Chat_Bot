import re
import random

# Define some sample patterns and responses
patterns = {
    r'hi|hello|hey': ['Hello!', 'Hi there!', 'Hey! How can I help you?'],
    r'how are you': ['I am a chatbot, I am always functioning!', 'I am doing great, thanks for asking!'],
    r'what is your name': ['I am a chatbot without a name, but you can call me Bot!'],
    r'bye|goodbye|see you': ['Goodbye!', 'Take care!', 'See you soon!'],
    r'(.*) your favorite (.*)': ['I do not have personal preferences, but I love to help!', 'I enjoy making conversations better!'],
    r'(.*) weather like': ['I am not connected to the internet to check the weather right now.', 'I cannot provide weather updates at the moment.'],
    r'help': ['I am here to assist you. Ask me anything!', 'How can I assist you today?'],
    r'(.*) (location|city)': ['I am based in the digital world.', 'I exist in the cloud, without a physical location!'],
    r'who created you': ['I was created by a developer using Python!', 'Some skilled developers built me with love!'],
    r'(.*)': ['Interesting! Can you tell me more?', 'Hmm, let me think about that...', 'Tell me more!']
}

# Function to get a response from the chatbot based on user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for better matching
    for pattern, responses in patterns.items():
        match = re.match(pattern, user_input)
        if match:
            return random.choice(responses)
    return "I don't understand that yet."

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if re.match(r'bye|goodbye|see you', user_input.lower()):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
