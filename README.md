# ASCII Art Rotation Animation

This Python script animates ASCII art by rotating it around a vertical axis using a simple cosine transformation. The animation runs in the terminal and gives a 3D-like effect by shifting characters horizontally based on their distance from the center.

## Features
- Rotate any ASCII art around its vertical axis.
- Runs smoothly in the terminal.
- Uses a cosine transformation to create a swinging effect.
- Easily customizable ASCII art.

## Preview
![](https://github.com/ballliekmvp/CLI-Ascii-animation-/blob/main/majidanimation.py%20-%20Code%20-%20Visual%20Studio%20Code%202025-02-12%2011-13-34.gif)

## Installation & Usage
### Prerequisites
Ensure you have Python 3 installed on your system.

### Running the Script
1. Clone the repository or download the script:
   ```sh
   git clone https://github.com/your-username/ascii-art-rotation.git
   cd ascii-art-rotation
   ```
2. Run the script:
   ```sh
   python3 rotate_ascii.py
   ```
3. Press `Ctrl + C` to exit the animation.

## Customizing the ASCII Art
You can replace the default ASCII art with your own. To do this:
1. Visit [this ASCII Art Generator](https://codepen.io/Mikhail-Bespalov/pen/JoPqYrz) to create your own ASCII art.
2. Copy the generated ASCII art.
3. Open `rotate_ascii.py` and replace the `ascii_art` string with your custom ASCII art.
4. Save the file and rerun the script.

## How It Works
- The script centers the ASCII art around a vertical axis.
- It applies a simple cosine transformation to shift characters horizontally based on their distance from the center.
- The animation updates in a loop, redrawing the rotated ASCII art with a slight delay for a smooth effect.

## Contributions
Feel free to fork this repository and submit pull requests for improvements!

## Author
Created by Majid Rebouh

