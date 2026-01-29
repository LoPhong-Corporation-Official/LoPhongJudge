# detect_anchors.py
import cv2
import numpy as np

def detect_black_squares(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, th = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    cnts, _ = cv2.findContours(
        th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    candidates = []

    for c in cnts:
        area = cv2.contourArea(c)
        if area < 200:
            continue

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.03 * peri, True)

        if 4 <= len(approx) <= 6:
            x, y, w, h = cv2.boundingRect(approx)
            ratio = w / h
            if 0.6 < ratio < 1.4:
                candidates.append((area, x, y, w, h))

    # ⚠️ QUAN TRỌNG: lấy 4 ô vuông LỚN nhất
    candidates = sorted(candidates, key=lambda x: x[0], reverse=True)
    anchors = candidates[:4]

    # trả về (x, y, w, h)
    return [(x, y, w, h) for (_, x, y, w, h) in anchors]
