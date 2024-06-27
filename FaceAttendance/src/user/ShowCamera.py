import cv2
from PIL import Image, ImageTk
import tkinter as tk


from src.user.DetectFace import DetectFace


def show_camera(frame_left, left_width, screen_height):
    cap = cv2.VideoCapture(0)  # Open webcam (change number if using multiple cameras)


    def update_frame():
        nonlocal frame_left
        nonlocal cap
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if ret:
            DetectFace(frame)

            # if status:
                # change_status_false()
            # FaceRecognizer()
            # Resize frame to fit frame_left dimensions
            frame = cv2.resize(frame, (left_width, screen_height))
            # Convert from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert frame to ImageTk format
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            # Update label with the new frame
            label_camera.config(image=img)
            label_camera.image = img  # Keep a reference
        frame_left.after(10, update_frame)  # Update every 10 milliseconds

    label_camera = tk.Label(frame_left)
    label_camera.pack(padx=0, pady=0)  # Add padding as needed
    update_frame()  # Start updating the frame
