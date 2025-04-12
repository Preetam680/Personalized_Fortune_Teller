# fortune.py (v1.0)
print("🔮 Welcome to Preetam Saha's Fortune Teller (21JE0695) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Preetam! Keep smiling. ✨")
elif mood == "sad":
    print("🌧️ Your fortune: Even on the smallest light shines in darkness. You're not alone bro.")
elif mood == "neutral":
    print("🌀 Your fortune: Even in neutrality, life subtly prepares you for joy. Enjoy the journey 😁")
else:
    print("🎭 Emotions are complex—try happy, sad, or neutral and I’ll try again!")
