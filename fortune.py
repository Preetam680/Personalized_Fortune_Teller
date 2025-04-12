# fortune.py (v1.1)
print("🔮 Welcome to Preetam Saha's Fortune Teller (21JE0695) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()
fortunes = {
    "happy": [
        "😄 Great things await you, Preetam! Keep smiling.",
        "🌞 Your joy is infectious. Share your light with the world!",
        "💫 Happiness fuels your journey. Ride the wave!",
        "🎉 Something amazing is around the corner—celebrate it in advance!",
        "🦋 Joy brings transformation. Fly high, Preetam!"
    ],
    "sad": [
        "💙 Even on the darkest days, you shine bright. Stay strong.",
        "🌈 After rain comes the rainbow. Hold on, Preetam.",
        "🌧️ This too shall pass—every storm has an end.",
        "🕯️ Light returns to those who carry hope in their hearts.",
        "🤗 You matter more than you know. Keep going."
    ],
    "neutral": [
        "🌿 A calm day is the perfect canvas for inspiration.",
        "🌀 Still waters run deep—big insights may be forming.",
        "📚 Balance today, brilliance tomorrow.",
        "⚖️ In neutrality lies clarity. Something powerful is aligning.",
        "🧘 Embrace the moment. Peace is power, Preetam."
    ],
    "stressed": [
        "🧠 Breathe, Preetam. You’re doing better than you think.",
        "💎 Pressure builds diamonds—you’re becoming unbreakable.",
        "📦 Take one task at a time. You’ve got this!",
        "🔥 You're strong. Don’t let stress dim your spark.",
        "🧘‍♂️ Calm is your secret weapon—use it wisely."
    ]
}
if mood in fortunes:
    print("✨ Your fortune:", random.choice(fortunes[mood]), "✨")
else:
    print("🎭 Emotions are complex—try happy, sad, or neutral and I’ll try again!")
