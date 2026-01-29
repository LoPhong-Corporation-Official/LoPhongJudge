# debug_zones.py
import cv2
from detect_zones import detect_zones

img = cv2.imread(r"D:\LoPhongJudge\backend\test\testcase\test2.png")
zones = detect_zones(r"D:\LoPhongJudge\backend\test\testcase\test2.png")

for name, (x, y, w, h) in zones.items():
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
    cv2.putText(img, name, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

cv2.imshow("ZONES", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
