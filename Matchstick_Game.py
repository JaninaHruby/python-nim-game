import tkinter as tk
from PIL import Image, ImageTk
from random import choice
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

length = range(21, 30)
matches = choice(length)


# Function to display matches
def display_matches():

    for widget in match_frame.winfo_children():
        widget.destroy()

    # Show image for each match

    for i in range(1, matches + 1):
        image_label = tk.Label(match_frame, image=image_tk)
        image_label.pack(side="left")

    # Display match count
    match_count = tk.Label(
        match_frame,
        text=matches,
        font=("Comic Sans", 24),
    )
    match_count.pack()


# Function to take matches
def take_matches(amount):
    global matches

    # Player draws
    matches -= amount
    display_matches()

    if matches <= 1:
        message_label.config(text="Game over. PC has lost!")
        return

    # Disable buttons while PC is playing
    one_button.config(state="disabled")
    two_button.config(state="disabled")
    three_button.config(state="disabled")

    # Calculate PC move
    if matches % 4 == 0: pc_move = 3
    elif matches % 4 == 1: pc_move = 1
    elif matches % 4 == 2: pc_move = 1
    else: pc_move = 2

    def pc_done():
        global matches
        matches -= pc_move
        display_matches()

        if matches <= 1:
            message_label.config(text=f"PC takes {pc_move}. You lost!")
        else:
            message_label.config(text=f"PC took {pc_move}. Your turn!")
            one_button.config(state="normal")
            two_button.config(state="normal")
            three_button.config(state="normal")

    root.after(800, pc_done)


# Create main window
root = tk.Tk()
root.title("Match Game")
root.geometry("1150x300")
root.option_add("*Font", "{Comic Sans MS}")

# Create frames to keep layout in order
header_frame = tk.Frame(root)
match_frame = tk.Frame(root)
button_frame = tk.Frame(root)

# Create and configure button/label widgets
quit_button = tk.Button(
    master=button_frame,
    text="Quit",
    command=root.destroy,
)

one_button = tk.Button(
    master=button_frame,
    text="One",
    command=lambda: take_matches(1),
)

two_button = tk.Button(
    master=button_frame,
    text="Two",
    command=lambda: take_matches(2),
)

three_button = tk.Button(
    master=button_frame,
    text="Three",
    command=lambda: take_matches(3),
)

# Create headline
headline = tk.Label(
    header_frame,
    text="Match Nim Game",
    font=("Comic Sans MS", 24),
)
headline.pack()

message_label = tk.Label(header_frame, text="Your turn!", font=("Comic Sans MS", 16))
message_label.pack(pady=(10, 0))

# Load image
image = Image.open(os.path.join(script_dir, "streichholz.png"))
image = image.resize((35, 35))
image_tk = ImageTk.PhotoImage(image)

display_matches()

# Pack buttons
one_button.pack(side="left", padx=5)
two_button.pack(side="left", padx=5)
three_button.pack(side="left", padx=5)
quit_button.pack(side="left", padx=20)

# Place widgets
header_frame.pack(pady=20)
match_frame.pack(pady=20)
button_frame.pack(pady=20)

root.mainloop()
