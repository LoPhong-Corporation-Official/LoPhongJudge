# read_number.py
# Đọc SBD hoặc mã đề theo cột (0–9)

import cv2
from omr import preprocess_cell, filled_ratio


def read_number(region_img, num_cols):
    """
    region_img : ảnh vùng SBD hoặc mã đề
    num_cols   : số chữ số (SBD=6, mã đề=3)
    """

    h, w = region_img.shape[:2]
    col_w = w // num_cols
    row_h = h // 10  # 0–9

    result = ""

    for c in range(num_cols):
        scores = []

        for d in range(10):
            x = c * col_w
            y = d * row_h

            cell = region_img[y:y+row_h, x:x+col_w]
            if cell.size == 0:
                scores.append(0)
                continue

            thresh = preprocess_cell(cell)
            score = filled_ratio(thresh)
            scores.append(score)

        max_score = max(scores)
        second = sorted(scores)[-2]

        if max_score < 0.15:
            result += "X"
        elif second > 0.12:
            result += "X"
        else:
            result += str(scores.index(max_score))

    return result
