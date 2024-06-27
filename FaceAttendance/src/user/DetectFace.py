import json

import cv2
import time

from src.user.FaceRecognizer import FaceRecognizer
from src.utils.audio_utils import play_audio

# Global variables to control audio playback timing
sound_played = False
last_played_time = time.time()

# Function to detect faces in a frame
def DetectFace(frame):
    global sound_played, last_played_time

    if frame is None:
        return frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade for user detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=15, minSize=(30, 30))
    if len(faces) > 0:
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Save the frame with rectangles (if needed)

        # Check if enough time has passed since last sound played
        current_time = time.time()
        if current_time - last_played_time > 10:

            cv2.imwrite("assets/image/image.jpg", frame)
            play_audio("assets/audio/DangNhanDang.mp3")
            sound_played = True
            last_played_time = current_time
            employee_id = FaceRecognizer()

            if employee_id:
                data = read_json()
                employee = find_employee_by_id(data, employee_id)
                employee["image"] ="assets/image/image.jpg"
                write_person_json(employee)

    return frame

def read_json ():
    try:
        with open("data.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
            # print(data)
            return data
    except IOError as e:
        print(f"Error reading 'person.json': {e}")
        return

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in 'person.json': {e}")
        return
def find_employee_by_id(employees, id):
    for employee in employees:
        if str(employee.get("ID")) == id:

            # print(f"Employee found: {employee}")
            return employee
    return None

def write_person_json(employee):
    try:
        with open('person.json', 'w', encoding='utf-8') as f:
            json.dump(employee, f, indent=4)
    except IOError as e:
        print("Error saving data:", e)