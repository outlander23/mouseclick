from pynput.mouse import Controller, Button
import pyautogui
import time
from random import randint

# Create a mouse controller instance
mouse = Controller()

print("Clicking at the current mouse position every 21 to 30 seconds...")

while True:
    # Get the current mouse position
    x, y = pyautogui.position()
    
    # Move the mouse to the specified coordinates
    mouse.position = (x, y)
    
    # Perform a left mouse click
    mouse.click(Button.left, 1)
    
    # Print a message indicating the click was performed
    print(f'Clicked at ({x}, {y})')
    
    # Wait for a random time between 21 and 30 seconds before the next click
    t = randint(21, 30)
    print(f'Waiting for {t} seconds before the next click...')
    time.sleep(t)

