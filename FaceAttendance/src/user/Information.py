import tkinter as tk
from PIL import Image, ImageTk
import json

def information(frame_right, right_width, screen_height):
    info_frame = tk.Frame(frame_right, width=right_width, height=screen_height, bg='#08182b')

    def load_and_display_image(image_path):
        try:
            # Load the image using Pillow
            image = Image.open(image_path)

            # Resize the image to fit within the info_frame
            max_width = right_width - 20  # Adjust as necessary
            max_height = screen_height - 100  # Adjust as necessary
            image.thumbnail((max_width, max_height))

            # Convert the Image object into a Tkinter-compatible photo image
            photo = ImageTk.PhotoImage(image)

            # Create a label widget to display the image
            label_image = tk.Label(info_frame, image=photo, bg='white')
            label_image.image = photo  # Keep a reference to the image
            label_image.pack(pady=20)
        except FileNotFoundError:
            print(f"Image file '{image_path}' not found.")
            # Create a label to show the error message
            label_error = tk.Label(info_frame, text=f"Image file '{image_path}' not found.", font=("Helvetica", 12),
                                   bg='white', fg='red')
            label_error.pack(pady=20)
        except Exception as e:
            print(f"Error loading image: {e}")
            # Create a label to show the error message
            label_error = tk.Label(info_frame, text=f"Error loading image: {e}", font=("Helvetica", 12), bg='white',
                                   fg='red')
            label_error.pack(pady=20)

    def load_information():
        try:
            with open("person.json", 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = None

        # Clear any existing widgets in info_frame
        for widget in info_frame.winfo_children():
            widget.destroy()

        if data:
            info_frame.pack_propagate(False)  # Prevent resizing based on content
            info_frame.pack(fill=tk.BOTH, expand=True)  # Pack with filling and expansion

            label_title = tk.Label(info_frame, text="Information", font=("Helvetica", 28, "bold"), bg='white')
            label_title.pack(pady=10)

            # Load and display the image
            load_and_display_image(data.get('image', ''))

            label_id = tk.Label(info_frame, text="ID: " + str(data.get('ID', '')), font=("Helvetica", 16), bg='white')
            label_id.pack(pady=5)

            label_name = tk.Label(info_frame, text="Name: " + data.get('Name', ''), font=("Helvetica", 16), bg='white')
            label_name.pack(pady=5)

            # Create a frame to contain the buttons and center it horizontally
            # button_frame = tk.Frame(info_frame, bg='#08182b')
            # button_frame.pack(pady=(10, 20))  # Adding some vertical padding
            #
            # # Styling and sizing the buttons
            # button_change_image = tk.Button(button_frame, text="Try again", font=("Helvetica", 12), bg='#B22222',
            #                                 fg='white', width=15, height=2, bd=0, relief=tk.FLAT, cursor='hand2',
            #                                 command=try_again_action)
            # button_change_image.pack(side=tk.LEFT, padx=10)
            #
            # button_perform_action = tk.Button(button_frame, text="Ok", font=("Helvetica", 12), bg='#2196F3',
            #                                   fg='white', width=15, height=2, bd=0, relief=tk.FLAT, cursor='hand2',
            #                                   command=perform_action)
            # button_perform_action.pack(side=tk.LEFT, padx=10)
        else:
            show_welcome()

    def show_welcome():
        # Clear any existing widgets in info_frame
        for widget in info_frame.winfo_children():
            widget.destroy()

        label_title = tk.Label(info_frame, text="Welcome", font=("Helvetica", 28, "bold"), bg='white')
        label_title.pack(pady=(screen_height // 2 - 50, 10), anchor=tk.CENTER)  # Căn giữa theo chiều dọc
        info_frame.pack_propagate(False)  # Prevent resizing based on content
        info_frame.pack(fill=tk.BOTH, expand=True)  # Pack with filling and expansion

    # Initial load of information
    load_information()

    # Start checking for updates every second
    def update_information():
        load_information()
        frame_right.after(1000, update_information)

    update_information()

    def try_again_action():
        # Thực hiện hành động khi nhấn nút "Try again" ở đây
        print("Try again button clicked")

    def perform_action():
        # Thực hiện hành động khi nhấn nút "Ok" ở đây
        print("Ok button clicked")