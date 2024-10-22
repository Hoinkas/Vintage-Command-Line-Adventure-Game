"""
EXPERIMENT #1 By Darkhorse
app
"""

import tkinter as tk
from tkinter import messagebox  # Import the messagebox correctly
from gui import GameWindow

def show_about():
    # Function to show an "About" window
    messagebox.showinfo("About", "Old-School Adventure Game\nVersion 1.0\nCreated by GANG69")

def main():
    # Initialize Tkinter
    root = tk.Tk()
    root.title("Old-School Adventure Game")

    # Disable window resizing and maximize options
    root.resizable(False, False)

    # Set the Tkinter window size and background color (grey)
    root.geometry("600x600")  # Square window

    # Create and pack the game window (pygame canvas inside tkinter)
    game_window = GameWindow(root)
    game_window.pack()

    # Add top menu
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="About", command=show_about)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
