# debug_anchors.py
import cv2
from detect_anchors import detect_black_squares

img = cv2.imread(r"D:\LoPhongJudge\backend\test\testcase\test2.png")
squares = detect_black_squares(img)

print("Found anchors:", len(squares))

for (x, y, w, h) in squares:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow("ANCHORS", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
