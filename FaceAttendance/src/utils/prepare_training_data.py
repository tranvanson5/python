import os
import cv2
import numpy as np


def prepare_training_data(data_folder_path):
    # Load the user cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # List to hold all subject faces and labels
    faces = []
    labels = []

    # Dictionary to map label IDs to person names
    label_map = {}
    label_id = 0

    # Loop through each person in the training data folder
    for person_name in os.listdir(data_folder_path):
        person_dir = os.path.join(data_folder_path, person_name)

        # Assign a unique label ID to each person
        if person_name not in label_map.values():
            label_map[label_id] = person_name
            current_label_id = label_id
            label_id += 1
        else:
            # Find the label ID for the existing person
            current_label_id = [key for key, value in label_map.items() if value == person_name][0]

        for image_name in os.listdir(person_dir):
            if image_name.startswith('.'):
                if image_name.startswith('.'):
                    continue
            image_path = os.path.join(person_dir, image_name)
            image = cv2.imread(image_path)
            print(image_path)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect user in the image
            faces_rects = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

            # If a user is detected, add it to the training set
            for (x, y, w, h) in faces_rects:
                face = gray_image[y:y+h, x:x+w]
                faces.append(face)
                labels.append(current_label_id)

    return faces, labels, label_map

def train_face_recognizer(data_folder_path):
    # Prepare training data
    faces, labels, label_map = prepare_training_data(data_folder_path)

    # Convert labels to numpy array of integers
    labels = np.array(labels, dtype=np.int32)

    # Create an LBPH user recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Train the recognizer on the faces and labels
    recognizer.train(faces, labels)

    # Save the trained model and label map
    recognizer.save('../assets/train/face_recognizer.yml')
    np.save('../../assets/train/label_map.npy', label_map)

    print("Training completed and model saved.")

# Example usage
train_face_recognizer('../../assets/dataset')
