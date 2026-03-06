# 💡 The Matchstick Project: From Challenge to Solution

## The Story Behind It

You don't give your partner a coding challenge unless you're prepared to be outperformed. 😏

My husband handed me an assignment from his engineering studies. Casually mentioned that back then, someone who already knew how to code took it further than he did. Built a GUI apparently. My husband didn't.

Ha! Challenge accepted.

I love a bit of competition, and if I get to show my husband how far I've come and he looks proud? That's the cherry on top. 🍒

So after the logic was finally working (and yes, I did struggle with it at first and had to talk it through with my study buddies before it clicked 😅), I started teaching myself Tkinter to build a GUI. That topic wasn't even on the curriculum for another few weeks. But once the ambition kicks in, there's no stopping me. 🔥

## 🎮 The Game

A classic Nim game against the computer. You take turns removing 1, 2 or 3 matchsticks. Whoever has to take the last one loses.

The computer uses a mathematical strategy based on modular arithmetic to play optimally. So if you know the math, you'll see what's going on. If not, it's a pretty tough opponent. 😄

## 🏗 Project Status

This project tracks my journey from a pure logic concept to a full graphical application.

- ✅ Mathematical winning strategy (backend logic)
- ✅ Dynamic image generation with Pillow & Matplotlib
- ✅ Full GUI with Tkinter (computer opponent included!)
- ✅ English version of the game
- ⬜ "Invincible Mode" (coming eventually… maybe)

## 🛠 What I Learned (The Hard Way)

The biggest lesson? Users don't follow instructions.

I was so excited to show my husband the finished game. And what does he do? Immediately starts clicking the buttons so fast that the computer can't even keep up with its "thinking" delay. I had built that in so it looks like the computer is actually considering its move. Nope. Broken in seconds.

To make it worse, I had flipped the win logic. So he just kept getting "You lost!" messages. Well, that's what you get for stress testing my buttons! 😬

In the end I greyed out the buttons while the computer is "thinking", so he's forced to slow down. Problem solved.

That whole experience taught me the importance of proper error handling and input validation. The notebook version catches invalid inputs gracefully without crashing. The Tkinter version sidesteps the problem entirely because buttons only let you make valid moves. 

I also had a fun time figuring out why Pillow wouldn't work on my Mac. Turns out, having multiple Python installations is a great way to question your sanity. The fix? Making sure the right Python interpreter actually knows about the installed packages. Lesson learned.

## 📁 Files

| File | What it does |
|------|-------------|
| `Streichholzspiel.ipynb` | The original notebook where I built the logic step by step |
| `Matchstick_Nim.py` | The finished GUI version (English) |
| `streichholz.png` | The matchstick image used in the game |

## 💻 Tech Stack

Python 3 with Tkinter, Pillow, Matplotlib, NumPy, random

## 🚀 How to Run

1. Clone the repository
2. Make sure `streichholz.png` is in the same directory as the script
3. Install dependencies:
   ```bash
   pip install pillow matplotlib numpy
   ```
4. Run the GUI version:
   ```bash
   python Matchstick_Nim.py
   ```
5. Or explore the notebook: `Streichholzspiel.ipynb`
