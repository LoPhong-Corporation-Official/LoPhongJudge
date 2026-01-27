# omr.py
# OMR core – chỉ xử lý 1 ô trắc nghiệm
# Phù hợp phiếu tròn, tô bút bi/bút chì

import cv2
import numpy as np


def preprocess_cell(cell_img):
    """
    Tiền xử lý ảnh ô:
    - Grayscale
    - Blur nhẹ
    - Threshold đảo (tô = trắng)
    """
    gray = cv2.cvtColor(cell_img, cv2.COLOR_BGR2GRAY)

    # Blur nhẹ để gom nét tô
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Nhị phân hóa
    _, thresh = cv2.threshold(
        blur, 0, 255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    return thresh


def compute_filled_ratio(thresh_img):
    """
    Tính tỷ lệ pixel được tô
    """
    filled = cv2.countNonZero(thresh_img)
    total = thresh_img.shape[0] * thresh_img.shape[1]
    return filled / total


def crop_inner_circle(cell_img, crop_ratio=0.30):
    """
    Cắt bỏ viền, chỉ giữ phần TRONG hình tròn
    """
    h, w = cell_img.shape[:2]

    pad_y = int(h * crop_ratio)
    pad_x = int(w * crop_ratio)

    inner = cell_img[
        pad_y : h - pad_y,
        pad_x : w - pad_x
    ]

    return inner


def is_filled(cell_img, threshold=0.075, debug=False):
    """
    Xác định ô có được tô hay không

    threshold khuyến nghị:
    - 0.08 : tô rất nhạt
    - 0.10 : CHUẨN THI
    - 0.15 : tô rất đậm
    """

    # Ô lỗi
    if cell_img is None or cell_img.size == 0:
        return False

    # 1. Cắt trong hình tròn (QUAN TRỌNG NHẤT)
    cell_inner = crop_inner_circle(cell_img, crop_ratio=0.30)

    # 2. Threshold
    thresh = preprocess_cell(cell_inner)

    # 3. Tính ratio
    ratio = compute_filled_ratio(thresh)

    if debug:
        print(f"Filled ratio = {ratio:.3f}")
        cv2.imwrite("debug_cell_inner.png", cell_inner)
        cv2.imwrite("debug_thresh.png", thresh)

    return ratio >= threshold
# --- IGNORE ---