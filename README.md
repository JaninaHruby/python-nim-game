💡 The Matchstick Project: From Challenge to Solution
The Story Behind It
It all started with a challenge from my husband's old engineering studies. Even though he'd already finished the course, my ambition kicked in. I didn't just want to understand the math behind it — I wanted to build something you can actually play. What started as a peek into an old university assignment turned into a deep dive into game logic, GUI development and a LOT of debugging. 😅
🎮 The Game
A classic Nim game against the computer. You take turns removing 1, 2 or 3 matchsticks. Whoever has to take the last one loses.
Sounds simple? The computer uses a mathematical strategy based on modular arithmetic to play optimally. Good luck beating it. 😉
🏗 Project Status
This project tracks my journey from a pure logic concept to a full graphical application.

✅ Mathematical winning strategy (backend logic)
✅ Dynamic image generation with Pillow & Matplotlib
✅ Full GUI with Tkinter (computer opponent included!)
✅ English version of the game
⬜ "Invincible Mode" (coming eventually… maybe)

🛠 What I Learned (The Hard Way)
The biggest lesson? Users don't follow instructions. I had my husband test the game and he immediately started entering nonsense just to break it. Classic. 😂
That taught me the importance of proper error handling and input validation. The notebook version catches invalid inputs gracefully without crashing. The Tkinter version sidesteps the problem entirely — buttons only let you make valid moves.
I also had a fun time figuring out why Pillow wouldn't work on my Mac. Turns out, having multiple Python installations is a great way to question your sanity. The fix? Making sure the right Python interpreter actually knows about the installed packages. Lesson learned.
📁 Files

Streichholzspiel.ipynb — The original notebook where I built the logic step by step
Matchstick_Nim.py — The finished GUI version (English)
streichholz.png — The matchstick image used in the game

💻 Tech Stack
Language: Python 3
Libraries: Tkinter, Pillow, Matplotlib, NumPy, random
🚀 How to Run

Clone the repository
Make sure streichholz.png is in the same directory as the script
Install dependencies: pip install pillow matplotlib numpy
Run the GUI version: python Matchstick_Nim.py
Or explore the notebook: Streichholzspiel.ipynb
