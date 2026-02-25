import cv2
import mediapipe as mp
import numpy as np
import winsound
from database.database import save_drowsiness

frequency = 2500
duration = 800

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

count = 0


def eye_ratio(landmarks, p1, p2, p3, p4):

    vertical = np.linalg.norm(landmarks[p2] - landmarks[p3])
    horizontal = np.linalg.norm(landmarks[p1] - landmarks[p4])

    return vertical / horizontal



def detect_drowsiness(frame):

    global count

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(frame_rgb)

    drowsy=False

    if results.multi_face_landmarks:

        h,w,_=frame.shape

        for face_landmarks in results.multi_face_landmarks:

            landmarks=[]

            for lm in face_landmarks.landmark:
                landmarks.append([int(lm.x*w),int(lm.y*h)])

            landmarks=np.array(landmarks)

            leftEAR = eye_ratio(landmarks,33,159,145,133)
            rightEAR = eye_ratio(landmarks,362,386,374,263)

            ear=(leftEAR+rightEAR)/2


            cv2.putText(frame,
                        f"EAR: {round(ear,2)}",
                        (20,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,255,0),2)

            cv2.putText(frame,
                        f"COUNT: {count}",
                        (20,90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,255,255),2)


            # Eyes closed
            if ear < 0.28:

                count += 1

                if count > 10:

                    drowsy=True

                    cv2.putText(frame,
                        "DROWSINESS DETECTED",
                        (20,140),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,0,255),
                        3)


                    # Continuous alarm
                    winsound.Beep(frequency,duration)

                    # Continuous database save
                    save_drowsiness()


            else:

                count=0


    return frame,drowsy