# Digital Clock (Tkinter)

A simple Python desktop application that displays a live digital clock with the current time and date, centered on top of a full-window background image.

## Overview

This project uses the Tkinter GUI toolkit and the `time` module to create a real-time digital clock.  
The window size automatically matches the background image, and the clock text is centered with a custom font and color.

## Features

- Live digital clock updated every second  
- Shows both time and date (day, month, year, weekday)  
- Custom full-window background image  
- Centered clock text with configurable font, color, and style  

## Requirements

- Python 3.x  
- Tkinter (comes bundled with most standard Python installations)  
- A PNG image file to use as the background  

## Installation

1. Install Python 3 if it is not already installed.
2. Clone this repository or download the project files.
3. Place your background image on your system and note its full path.
4. Open the script file (e.g. `digital_clock.py`) in a code editor.

## Configuration

In the script, update the background image path:


You can also customize:

- Font family, size, and style:


- Text color:


- Time/date format:


## How It Works

- Creates a Tkinter window titled "Digital Clock".
- Loads a background image using `PhotoImage` and displays it on a `Canvas`.
- Sets the window size based on the image width and height.
- Creates a centered text item on the canvas to display the time and date.
- Uses an `update_time()` function with `time.strftime()` to get the current time and date.
- Updates the text every 1000 ms using `root.after(1000, update_time)`.
- Starts the Tkinter event loop with `root.mainloop()`.

## Running The App

1. Open a terminal or command prompt in the project directory.
2. Run:
3. A window will appear with your background image and a live digital clock centered on the screen.
4. Close the window to exit the application.

