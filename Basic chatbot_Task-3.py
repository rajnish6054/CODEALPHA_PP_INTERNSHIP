import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import random

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Define the greeting responses
greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]

# Define the farewell responses
farewells = ["Goodbye!", "See you later!", "Bye!", "Have a nice day!"]

# Define the conversation responses
conversation_responses = {
    "how are you": ["I'm doing well, thanks for asking!", "Doing great, how about you?"],
    "what's up": ["Not much, just chatting with you!", "Just hanging out, how about you?"],
    "tell me a joke": ["Why can't a bicycle stand up by itself? It's two tired!", "What do you call a fake noodle? An Impasta!"],
    "default": ["I'm afraid I don't understand. Could you please rephrase your question?", "I'm not sure I follow. Could you provide more context?"]
}

# Define the chatbot function
def chatbot():
    print(random.choice(greetings))
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot:", random.choice(farewells))
            break
        
        # Lemmatize the user input
        lemmatized_input = [lemmatizer.lemmatize(word) for word in user_input.split()]
        
        # Check for matching responses
        found_response = False
        for key in conversation_responses:
            if key in user_input:
                print("Chatbot:", random.choice(conversation_responses[key]))
                found_response = True
                break
        
        if not found_response:
            print("Chatbot:", random.choice(conversation_responses["default"]))

# Start the chatbot
chatbot()