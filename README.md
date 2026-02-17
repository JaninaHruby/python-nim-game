💡 The Matchstick Project: From Challenge to Solution
The Story Behind the Project
This project started when I came across a challenging assignment from my husband’s former engineering studies. Even though he had already completed the course, my ambition was sparked. I didn't just want to understand the mathematical logic behind it; I wanted to build a version that was visually engaging and technically robust. What began as a look into an old university project turned into an intensive lesson in User Experience and stable programming for me.

🏗 Project Status: Work in Progress
This project is actively being developed as part of my journey into IT. It tracks my progress from a pure logic concept to a full graphical application.

Roadmap:

[x] Mathematical winning strategy (Backend logic)

[x] Dynamic image generation with Pillow & Matplotlib

[ ] In Progress: Transition from console input to a full GUI (Tkinter)

[ ] Implementation of an "Invincible Mode"

🎮 The Game & Logic
A classic Nim game against the computer.

The Challenge: The computer uses a mathematical strategy based on modular arithmetic (matches % 4) to ensure it plays optimally.

The Visuals: Instead of plain text, the program dynamically generates a grid of matchstick graphics for every move, making the game state intuitive to follow.

🛠 What I Learned (The Hard Way)
The most important takeaway was making the code "user-proof" through real-world testing.

User Testing: I had my husband test the game repeatedly. This revealed a crucial insight: users don't always follow instructions—they might enter text or invalid numbers just to see what happens.

The Solution: I implemented strict error handling (try-except) and validation logic. The program now handles invalid data types and rule violations gracefully without crashing.

Asset Management: Learning how to correctly integrate and scale external image files within a Python environment.

💻 Tech-Stack
Language: Python 3

Libraries: Matplotlib, Pillow, NumPy, math, random

🚀 How to Run
Clone the repository.

Ensure streichholz.png is in the same directory.

Install dependencies: pip install numpy pillow matplotlib

Run the game: python nim_spiel.py
