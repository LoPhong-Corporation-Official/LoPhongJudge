from detect_zones import detect_zones
from read_number import read_number
from omr import read_row
import cv2


def process_form(image_path):
    img = cv2.imread(image_path)
    zones = detect_zones(image_path)

    # SBD
    x, y, w, h = zones["sbd"]
    sbd = read_number(img[y:y+h, x:x+w], num_cols=6)

    # Mã đề
    x, y, w, h = zones["ma_de"]
    ma_de = read_number(img[y:y+h, x:x+w], num_cols=3)

    # Đáp án
    x, y, w, h = zones["answers"]
    answer_region = img[y:y+h, x:x+w]

    # đọc giống trước
    # ...

    return {
        "sbd": sbd,
        "ma_de": ma_de,
        # "answers": answers
    }
    # Placeholder for answers reading logic
    # --- IGNORE ---
    # End of placeholder