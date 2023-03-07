import cv2
import mediapipe as mp
import time
import ArduinoControl as cnt

print(cv2.__version__)
width = 720
height = 480
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 5)
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPEG'))

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
tipIds = [4, 8, 12, 16, 20]
cTime = 0
pTime = 0
def texts(num, led):
    cv2.putText(frame, num, (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
    cv2.putText(frame, led, (100, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)


while True:
    ret, frame = cap.read()
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    # print(result.multi_hand_landmarks)
    frame.flags.writeable = True
    lmList = []
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                # print(id, lm)
                h, w, c = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
            mpDraw.draw_landmarks(frame, handlms, mpHands.HAND_CONNECTIONS)
            print(lmList)
    fingers = []
    if len(lmList) != 0:
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        total = fingers.count(1)
        print(total)
        cnt.led(total)
        if total == 0:
            texts('0', 'led')
        elif total == 1:
            texts('1', 'led')
        elif total == 2:
            texts('2', 'leds')
        elif total == 3:
            texts('3', 'leds')
        elif total == 4:
            texts('4', 'leds')
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (0, 60), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.imshow('webcam', frame)
    cv2.moveWindow('webcam', 50, 0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()