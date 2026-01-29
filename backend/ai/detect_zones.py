# detect_zones.py
import cv2
from detect_anchors import detect_black_squares


def detect_zones(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Không đọc được ảnh")

    squares = detect_black_squares(img)
    if len(squares) < 4:
        raise ValueError("Không đủ anchor")

    squares = sorted(squares, key=lambda x: (x[1], x[0]))

    tl, tr = squares[0], squares[1]
    bl, br = squares[-2], squares[-1]

    left = tl[0]
    right = tr[0] + tr[2]
    top = tl[1]
    bottom = bl[1] + bl[3]

    width = right - left
    height = bottom - top

    return {
        "sbd": (
            int(left + width * 0.10),
            int(top + height * 0.28),
            int(width * 0.25),
            int(height * 0.38)
        ),
        "ma_de": (
            int(left + width * 0.40),
            int(top + height * 0.28),
            int(width * 0.15),
            int(height * 0.38)
        ),
        "answers": (
            int(left + width * 0.60),
            int(top + height * 0.28),
            int(width * 0.33),
            int(height * 0.60)
        )
    }
