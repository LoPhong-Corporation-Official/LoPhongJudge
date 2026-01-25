# layout.py
# Mô tả vị trí các vùng theo pixel (test 1 lần)

ANSWER_START_X = 200
ANSWER_START_Y = 600

ROW_HEIGHT = 45        # khoảng cách giữa các câu
COL_WIDTH = 55         # khoảng cách A B C D

NUM_QUESTIONS = 40

# mapping cột → đáp án
CHOICES = ["A", "B", "C", "D"]
def get_answer_position(question_number, choice_index):
    x = ANSWER_START_X + choice_index * COL_WIDTH
    y = ANSWER_START_Y + question_number * ROW_HEIGHT
    return (x, y)
#This function returns the pixel position of a given answer choice for a specific question number.
# Ví dụ: câu 0 đáp án A → (200, 600)
# câu 1 đáp án C → (200 + 2*55, 600 + 1*45) = (310, 645)
# câu 39 đáp án D → (200 + 3*55, 600 + 39*45) = (365, 2355)
# backend/test/test_ocr.py
#Nhưng chưa dùng