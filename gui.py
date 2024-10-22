"""
EXPERIMENT #1 By Darkhorse
gui
"""

import tkinter as tk
import pygame
from PIL import Image, ImageTk

class GameWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Set up the main window layout
        self.create_layout(parent)

        # Initialize the Pygame environment
        self.init_pygame_canvas()

    def create_layout(self, parent):
        # Create the main layout areas: pygame canvas, buttons, and command console

        # Pygame canvas inside a Tkinter Canvas widget
        self.canvas = tk.Canvas(self, width=600, height=400)
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Buttons for Inventory, Status, etc.
        self.inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
        self.inventory_button.grid(row=1, column=0, padx=10, pady=10)

        self.status_button = tk.Button(self, text="Status", command=self.show_status)
        self.status_button.grid(row=1, column=1, padx=10, pady=10)

        # Command-line entry at the bottom
        self.command_entry = tk.Entry(self, width=50)
        self.command_entry.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        submit_button = tk.Button(self, text="Submit", command=self.handle_command)
        submit_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    def init_pygame_canvas(self):
        # Initialize Pygame and create a pygame surface
        pygame.init()

        # Create a pygame surface with the desired dimensions
        self.screen = pygame.Surface((600, 400))
        self.screen.fill((0, 0, 0))  # Black background for the canvas

        # Set up a basic message
        self.display_message("Hello Adventurers!")

        # Schedule a repeated task to refresh the canvas
        self.update_canvas()

    def update_canvas(self):
        # Convert the Pygame surface to a format that Tkinter can handle
        image_data = self.pygame_to_image(self.screen)
        self.image = ImageTk.PhotoImage(image=image_data)

        # Add the image to the Tkinter canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Repeat this every 30ms to keep the Pygame canvas active
        self.after(30, self.update_canvas)

    def pygame_to_image(self, surface):
        # Convert the Pygame surface to a format Pillow understands (RGB)
        image_string = pygame.image.tostring(surface, "RGB")
        image = Image.frombytes("RGB", surface.get_size(), image_string)
        return image

    def display_message(self, message):
        # Set up Pygame font and display text
        font = pygame.font.Font(None, 48)
        text = font.render(message, True, (255, 255, 255))  # White text
        
        # Position text in the center of the canvas
        text_rect = text.get_rect(center=(300, 200))
        self.screen.blit(text, text_rect)

    def handle_command(self):
        # This function processes the command-line input
        command = self.command_entry.get()
        print(f"Command entered: {command}")
        self.command_entry.delete(0, 'end')

    def show_inventory(self):
        # Example inventory check
        print("Inventory: Sword, Shield, Potion")

    def show_status(self):
        # Example status check
        print("Status: Health 100%, Mana 50%")
