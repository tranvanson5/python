import cv2
import numpy as np

from src.utils.audio_utils import play_audio
from src.utils.write_person_json import write_person_json


confidence_threshold = 50


def FaceRecognizer():

    # Load pre-trained user detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load pre-trained user recognition model
    face_recognizer = cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=5, grid_x=1, grid_y=1)
    face_recognizer.read('assets/train/face_recognizer.yml')

    # Load label map
    label_map = np.load('assets/train/label_map.npy', allow_pickle=True).item()

    # Load the input image
    img = cv2.imread('assets/image/image.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Recognize the user using the trained model
        label, confidence = face_recognizer.predict(gray[y:y + h, x:x + w])

        # Get the name corresponding to the label
        person_name = label_map[label]
        # Draw a rectangle around the detected user
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # if person_name :
        #     play_audio("C:/Users/drive/Desktop/FaceAttendance/assets/audio/NhanDangThanhCong.mp3")
        #     return person_name
        # else:
        #     play_audio("C:/Users/drive/Desktop/FaceAttendance/assets/audio/NhanDangThatBai.mp3")
        #     return
        if confidence < confidence_threshold:
            # Draw a red rectangle around the user
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # Display "Unknown" text on the frame
            cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            # Optionally, play failure recognition sound
            play_audio("assets/audio/NhanDangThatBai.mp3")
            write_person_json(None)

            return
        else:
            # name = label_map[label_id]
            # cv2.rectangle(img, (x, y), (x + w, y + h), (36, 255, 12), 2)
            # cv2.putText(frame, f"{name} ({confidence:.2f})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12),2)
            # Play success recognition sound
            play_audio("assets/audio/NhanDangThanhCong.mp3")
            write_person_json(None)

            return person_name
