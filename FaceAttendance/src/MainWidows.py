import tkinter as tk

from src.user.Information import information
from src.user.ShowCamera import show_camera


def MainWindows():
    root = tk.Tk()
    root.title("Main Window")

    # Set the window to fullscreen
    root.attributes('-fullscreen', True)
    
    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Define the size of the left and right sections
    left_width = int(screen_width * 0.6)
    right_width = int(screen_width * 0.4)

    # Create frames for left and right sections
    frame_left = tk.Frame(root, width=left_width, height=screen_height)
    frame_right = tk.Frame(root, width=right_width, height=screen_height, bg='white')

    # Pack frames to fill the window
    frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Call show_camera function from camera_display.py to display webcam feed in the left section
    show_camera(frame_left, left_width, screen_height)
    information(frame_right,right_width,screen_height)

    root.mainloop()

