import cv2
import numpy as np
import pymysql
import face_recognition as fr
import mediapipe as mp
import pickle

drawingutil = mp.solutions.drawing_utils
drwaingstyle = mp.solutions.drawing_styles
video = cv2.VideoCapture(0)
mpfacerecog = mp.solutions.face_detection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='database_name'
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM face_encodings")
rows = cursor.fetchall()
default_encodings=np.zeros(128)
with mpfacerecog.FaceDetection(min_detection_confidence=0.5, model_selection=0) as facedetectL:
    while True:
        success, img = video.read()
        if not success:
            break

        results = facedetectL.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        for landmarks in results.detections:
            box = landmarks.location_data.relative_bounding_box
            ih, iw, _ = img.shape
            x, y, w, h = int(box.xmin * iw), int(box.ymin * ih), int(box.width * iw), int(box.height * ih)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            face_location = [(y, x + w, y + h, x)]
            encoding = fr.face_encodings(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),face_location)
            for row in rows:
                s_encodings = pickle.loads(row[2])

                if encoding:
                    distance = fr.face_distance([s_encodings], encoding[0])
                    if distance < 0.6:
                        cv2.putText(img, f"{row[1]}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255),
                                2)
                else:
                    distance = fr.face_distance([s_encodings], default_encodings)

            score = landmarks.score[0]

            cv2.putText(img, f'{int(score * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow("VIDEO", img)
    video.release()
    cv2.destroyAllWindows()
