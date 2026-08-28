import cv2
import mediapipe as mp
import math
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Inicializar cámara y detector de manos
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Configurar control de volumen de Windows (PyCaw)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
vol_range = volume.GetVolumeRange()  # Rango mínimo y máximo de volumen (en dB)
min_vol = vol_range[0]
max_vol = vol_range[1]

while cap.isOpened():
    success, img = cap.read()
    if not success:
        break

    # Convertir la imagen de BGR a RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            h, w, c = img.shape
            # Obtener coordenadas del pulgar (punto 4) y del índice (punto 8)
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            
            x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
            x2, y2 = int(index_tip.x * w), int(index_tip.y * h)
            
            # Dibujar círculos y línea guía entre los dedos
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            
            # Calcular la distancia entre los dos dedos
            length = math.hypot(x2 - x1, y2 - y1)
            
            # Convertir la distancia a un rango de volumen del sistema
            vol = np.interp(length, [30, 250], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(vol, None)

    # Mostrar la ventana en pantalla
    cv2.imshow("Control de Volumen con IA", img)
    
    # Presionar la tecla 'q' para salir del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()