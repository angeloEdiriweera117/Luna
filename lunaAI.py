#lunaAI
import random

# Predefined responses based on keywords
responses = {
    "hello": ["Hello there. How are you feeling today?", "Hi! I'm here to listen. What's on your mind?"],
    "sad": ["I'm sorry you're feeling sad. Want to talk more about it?", "Sadness is tough. Do you want to tell me what's causing it?"],
    "happy": ["That's great to hear! What’s making you feel happy?", "I'm glad you're feeling good! Want to share more?"],
    "angry": ["It's okay to feel angry. Can you tell me what's making you feel that way?", "Anger is valid. Let's talk about it."],
    "anxious": ["Anxiety can be overwhelming. Want to explore what's making you anxious?", "Let's take a deep breath. What’s been worrying you?"],
    "bye": ["Take care! I'm always here if you want to talk.", "Goodbye! Remember, you're not alone."],
    "default": ["Tell me more about that.", "How does that make you feel?", "Can you elaborate on that?"]
}

# Function to find keyword in input and respond
def get_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])
    return random.choice(responses["default"])

def main():
    print("TherapistBot: Hi, I'm your virtual therapist. What's on your mind?")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("TherapistBot:", get_response(user_input))
            break
        response = get_response(user_input)
        print("TherapistBot:", response)

if __name__ == "__main__":
    main()




