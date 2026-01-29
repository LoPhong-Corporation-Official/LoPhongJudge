# omr.py
# Core OMR engine – dùng cho đáp án, SBD, mã đề

import cv2
import numpy as np


def preprocess_cell(cell):
    """
    Chuẩn hóa 1 ô trắc nghiệm
    """
    gray = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.threshold(
        blur, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )[1]

    return thresh


def filled_ratio(thresh):
    """
    Tỉ lệ pixel đen
    """
    return cv2.countNonZero(thresh) / thresh.size


def read_row(cells):
    """
    Đọc 1 hàng đáp án A B C D
    cells: list ảnh [A, B, C, D]
    """

    scores = [filled_ratio(preprocess_cell(c)) for c in cells]

    max_score = max(scores)
    second_score = sorted(scores)[-2]

    # DEBUG khi cần
    # print(scores)

    # Không tô
    if max_score < 0.15:
        return "BLANK"

    # Tô nhiều hơn 1 ô
    if second_score > 0.12:
        return "INVALID"

    return "ABCD"[scores.index(max_score)]
# Fixed indentation issues