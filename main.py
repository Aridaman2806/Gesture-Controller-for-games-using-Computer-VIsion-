import cv2
import mediapipe as mp
from pynput.keyboard import Controller

mp_hands = mp.solutions.hands.Hands()
keybord = Controller()

cam = cv2.VideoCapture(0)
x1=0
x2=0
y1=0
y2=0

while(True):
    _, image = cam.read()
    image_h , image_w , image_d = image.shape
    image = cv2.flip(image,1)

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    find_hands = mp_hands.process(rgb)
    all_hands = find_hands.multi_hand_landmarks

    if all_hands:
        main_hand = all_hands[0]
        main_hand_landmark = main_hand.landmark

        for id , landmark in enumerate(main_hand_landmark):
            x = int(landmark.x * image_w)
            y = int(landmark.y * image_h)

            if id == 12:
                x1=x
                y1=y
            if id == 0:
                x2=x
                y2=y

        Dist_horizotal = 0
        Dist_horizontal = x1 - x2

        Dist_vertical = 0
        Dist_vertical = y1-y2

        if Dist_vertical > -140 and Dist_vertical !=0:
          keybord.release('d')
          keybord.release('a')
          keybord.release('w')
          keybord.press('s')
          print("S")
    
        if Dist_vertical < -200 and Dist_vertical != 0:
          keybord.release('s')
          keybord.release('d')
          keybord.release('a')
          keybord.press('w')
          print("W")

        if (Dist_horizontal < -60 and Dist_horizontal != 0):
          keybord.release('s')
          keybord.release('d')
          keybord.press('w')
          keybord.press('a')
          print("A")

        if (Dist_horizontal > 55 and Dist_horizontal != 0):
          keybord.release('s')
          keybord.release('a')
          keybord.press('w')
          keybord.press('d')
          print("D")
    
    else:
        print("none")
        keybord.release('a')
        keybord.release('w')
        keybord.release('s')     
        keybord.release('d')
    if image is not None:
       cv2.imshow("Gesture" , image)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()
