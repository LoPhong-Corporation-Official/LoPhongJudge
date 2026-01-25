import cv2
from layout import *

def is_filled(cell_img, threshold=0.45):
    """
    Kiểm tra ô có được tô không
    """
    gray = cv2.cvtColor(cell_img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    filled = cv2.countNonZero(th)
    total = th.shape[0] * th.shape[1]

    return filled / total > threshold


def read_answers(image_path):
    img = cv2.imread(image_path)
    answers = {}

    for q in range(NUM_QUESTIONS):
        y = ANSWER_START_Y + q * ROW_HEIGHT

        for i, choice in enumerate(CHOICES):
            x = ANSWER_START_X + i * COL_WIDTH

            cell = img[y:y+40, x:x+40]

            if cell.size == 0:
                continue

            if is_filled(cell):
                answers[str(q + 1)] = choice

    return answers
