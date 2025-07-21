from textblob import TextBlob
import random

# Function to find your mood
def find_mood(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity  # ranges from -1 (sad) to +1 (happy)

    if score > 0.3:
        return "happy"
    elif score < -0.3:
        return "sad"
    else:
        return "neutral"

# Suggestions based on mood
def give_advice(mood):
    if mood == "happy":
        return random.choice([
            "That's wonderful! Keep smiling 😊",
            "Love your energy today!",
            "Enjoy your day and spread the happiness!"
        ])
    elif mood == "sad":
        return random.choice([
            "I'm here for you. Things will get better. 💛",
            "It's okay to feel this way. Take a deep breath.",
            "Try doing something that makes you feel calm, like music or a walk."
        ])
    else:
        return random.choice([
            "Thanks for sharing. Want to talk more?",
            "Let’s take a small moment to relax together.",
            "Would you like to try a short breathing exercise?"
        ])

# Fun mindfulness tip
def give_tip():
    tips = [
        "🧘 Try closing your eyes and take 3 deep breaths.",
        "🌳 Go outside and listen to the sounds around you.",
        "📓 Write down one good thing that happened today.",
        "💧 Slowly drink a glass of water and enjoy the moment."
    ]
    return random.choice(tips)

# Main chatbot function
def start_chat():
    print("👋 Hello! I'm your AI Mental Health Friend.")
    print("Tell me how you're feeling. Type 'exit' to stop.\n")

    while True:
        user_input = input("🗣️  You: ")

        if user_input.lower() == "exit":
            print("👋 Goodbye! Take care of yourself.")
            break

        mood = find_mood(user_input)
        advice = give_advice(mood)
        tip = give_tip()

        print(f"\n🤖 AI: {advice}")
        print(f"💡 Tip: {tip}\n")

# Start the program
start_chat()
