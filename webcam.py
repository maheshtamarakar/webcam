import cv2
import numpy as np
import pyautogui


yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
prev_y = 0
while True:
    ret, frame = cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#converting frame colour
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)#detect only this range, yellow_lower and upper pick up colour fron 'hsv'
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#detected white area from black screen in opencv
    for c in contours:
        area = cv2.contourArea(c)
        if area>300 and area<1000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if y < prev_y:
                pyautogui.press('space')
                for i in range(1000):
                    print(f'move down {i}')
                
            prev_y = y
    cv2.imshow('frame', frame)#showing whatever infront of camera

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()