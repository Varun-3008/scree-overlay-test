import cv2
import numpy as np
import pyautogui

# Function to get the color at a specific point
def get_color_at_point(x, y):
    # Capture the screen
    screen = np.array(cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR))

    # Get the color at the specified point
    color = screen[y, x]

    return color

# Function to simulate a mouse click at a point
def click_at_point(x, y):
    pyautogui.click(x, y)

# Example coordinates
read_x = 574
read_y = 708

clickx = 1248
clicky = 19
# Red color threshold
red_threshold = 100

while True:
    # Get the color at the specified point
    color = get_color_at_point(read_x, read_y)
    
    # Check if the color is red
    if color[2] > red_threshold and color[0] < red_threshold and color[1] < red_threshold:
        print("Red color detected at ({}, {})".format(read_x, read_y))
        click_at_point(clickx, clicky)
        click_at_point(646,374)
    else:
        print("not red")
    
    # Wait for a short duration before checking again
    # Adjust the duration based on your requirements
    pyautogui.sleep(0.5)

