import cv2
import mediapipe as mp
import pyautogui

capture = cv2.VideoCapture(0)
handDetector = mp.solutions.hands.Hands()
drawingUtils = mp.solutions.drawing_utils
screenWidth, screenHeight = pyautogui.size()
index_y = 0

while True:
    _, frame = capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frameHeight, frameWidth, _ = frame.shape
    output = handDetector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawingUtils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frameWidth)
                y = int(landmark.y * frameHeight)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screenWidth / frameWidth * x
                    index_y = screenHeight / frameHeight * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screenWidth / frameWidth * x
                    thumb_y = screenHeight / frameHeight * y
                    print('Outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 25:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
