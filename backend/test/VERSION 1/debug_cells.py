import cv2
from layout import *

img = cv2.imread(r"D:\LoPhongJudge\backend\test\form.png")

for q in range(3):  # test 3 câu đầu
    y = ANSWER_START_Y + q * ROW_HEIGHT

    for i, c in enumerate(CHOICES):
        x = ANSWER_START_X + i * COL_WIDTH
        cell = img[y:y+40, x:x+40]

        cv2.imwrite(f"dbg_q{q+1}_{c}.png", cell)
        print(f"Câu {q+1} đáp án {c} tại vị trí ({x}, {y})")


# Tạo ảnh debug các ô trả lời của 3 câu đầu
# Kết quả lưu trong backend/test/ như:
# dbg_q1_A.png, dbg_q1_B.png, dbg_q1_C.png, dbg_q1_D.png
# dbg_q2_A.png, dbg_q2_B.png, dbg_q2_C.png, dbg_q2_D.png
# dbg_q3_A.png, dbg_q3_B.png, dbg_q3_C.png, dbg_q3_D.png
# In ra tọa độ pixel của từng ô trả lời
# Ví dụ: Câu 1 đáp án A tại vị trí (200, 600)
# Câu 1 đáp án B tại vị trí (255, 600)
