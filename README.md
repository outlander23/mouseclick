# mouseclick
# Automatic Mouse Clicker

This Python script automatically clicks the mouse at its current position every 21 to 30 seconds. It is useful for scenarios where you need to keep an application active or simulate user interaction.

## How It Works

The script uses the `pynput` and `pyautogui` libraries to control the mouse and perform clicks at the current cursor position. The delay between each click is randomized between 21 and 30 seconds to mimic natural behavior.

### Key Features
- **Automatic Clicking:** The script clicks the mouse at its current position every 21 to 30 seconds.
- **Random Delay:** The delay between each click is randomized to make the clicking pattern less predictable.
- **Simple to Use:** Just run the script, and it will start clicking automatically.

## Requirements

Before running the script, make sure you have the required Python packages installed:

  ```bash
pip install pynput pyautogui
 ```

How to Use
Clone the Repository:

bash
```
git clone https://github.com/outlander23/mouseclick/.git
cd automatic-mouse-clicker
```

Run the Script:

``` bash
python auto_clicker.py
 ```
Behavior:

The script will continuously click at the current mouse position.
The delay between each click is randomized between 21 and 30 seconds.
You can stop the script at any time by pressing Ctrl + C.
