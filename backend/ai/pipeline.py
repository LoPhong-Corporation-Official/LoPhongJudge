import cv2
from detect_answer_region import detect_answer_region
from omr import is_filled

CHOICES = ["A", "B", "C", "D"]
NUM_QUESTIONS = 40

def read_answers_auto(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Không đọc được ảnh")

    # 1. AI detect vùng đáp án
    box = detect_answer_region(image_path)
    if box is None:
        raise ValueError("Không detect được vùng đáp án")

    x0, y0, w, h = box
    answer_region = img[y0:y0+h, x0:x0+w]

    # 2. Tính kích thước động
    row_h = h // NUM_QUESTIONS
    col_w = w // 4

    answers = {}

    for q in range(NUM_QUESTIONS):
        y = q * row_h

        for i, choice in enumerate(CHOICES):
            x = i * col_w
            pad_y = int(row_h * 0.30)
            pad_x = int(col_w * 0.30)

            cell = answer_region[
            y + pad_y : y + row_h - pad_y,
            x + pad_x : x + col_w - pad_x
            ]
          


            if cell.size == 0:
                continue

            if is_filled(cell):
                answers[str(q + 1)] = choice

    return answers
