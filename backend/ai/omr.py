import cv2
from layout import *

def is_filled(cell_img, threshold=0.5):
    """
    Kiểm tra ô có được tô hay không
    """
    gray = cv2.cvtColor(cell_img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(gray, 0, 255,
                          cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    filled_ratio = cv2.countNonZero(th) / (cell_img.size / 3)
    return filled_ratio > threshold


def read_answers(image_path):
    img = cv2.imread(image_path)
    answers = {}

    for q in range(NUM_QUESTIONS):
        y = ANSWER_START_Y + q * ROW_HEIGHT

        for i, choice in enumerate(CHOICES):
            x = ANSWER_START_X + i * COL_WIDTH

            cell = img[y:y+40, x:x+40]  # cắt ô
            if is_filled(cell):
                answers[str(q + 1)] = choice

    return answers
# Ví dụ sử dụng
# answers = read_answers("path_to_answer_sheet_image.jpg")
# print(answers)
# Trả về dict {số câu: đáp án}
