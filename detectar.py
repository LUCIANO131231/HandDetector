import cv2
import mediapipe as mp

# para inicializar mediapipe de google
mp_hands = mp.solutions.hands
hands = mp.hands.Hands(static_image_mode=False,
                       max_num_hands = 2,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

#funcion para detectar los dedos levantados (10)
def detectar_dedos(hand_landmarks):
    dedos = []
    tips_ids = [4,8,12,16,20]

    for i, tip in enumerate(tips_ids):
        if i == 0:
            if hand_landmarks.landmark[tip].x < hand_landmarks[tip - 1].x:
                dedos.append(1) #cuando levanta el dedo pulgar
            else:
                dedos.append(0) #cuando no levanta el dedo pulgar
        
        else:
            if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                dedos.append(1) #los demas dedos al levantar
            else:
                dedos.append(0) #los demas dedos no levantados
    return dedos