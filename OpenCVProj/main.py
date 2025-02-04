import cv2 as cv
import mediapipe as mp
import numpy as np

mp_hand = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hand.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2)

capture = cv.VideoCapture(0)

def pen(landmarks):
    hand1 = landmarks[0]
    hand2 = landmarks[1]

    index_tip_left = np.array([hand1.landmark[8].x, hand1.landmark[8].y])
    index_tip_right = np.array([hand2.landmark[8].x, hand2.landmark[8].y])

    left_thumb = np.array([hand1.landmark[4].x, hand1.landmark[4].y])  
    right_thumb = np.array([hand2.landmark[4].x, hand2.landmark[4].y]) 

    left_distance = np.linalg.norm(index_tip_left - left_thumb)
    right_distance = np.linalg.norm(index_tip_right - right_thumb)

    return left_distance < 0.07 or right_distance < 0.07

while capture.isOpened():
    success, frame = capture.read()
    if not success:
        break

    frame = cv.flip(frame, 1)
    rgb_frame= cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        landmark_list=[]
        for hand_landmarks in result.multi_hand_landmarks:
            landmark_list.append(hand_landmarks)
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)
        if pen(landmark_list):
            pass

    cv.imshow("Hey there ", frame)
    if cv.waitKey(1) & 0xFF == ord('a'):
        break

capture.release()
cv.destroyAllWindows()
