import cv2
import numpy as np
import os

def detect_answer_region(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Làm mịn + edge
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File không tồn tại: {image_path}")

    if img is None:
       raise ValueError(f"OpenCV không đọc được ảnh: {image_path}")
        # phần dưới giữ nguyên
        #blur = cv2.GaussianBlur(gray, (5, 5), 0)
        #edges = cv2.Canny(blur, 50, 150)
    # Detect circle (Hough Circle)
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=30,
        param1=50,
        param2=15,
        minRadius=8,
        maxRadius=20
    )

    if circles is None:
        return None

    circles = np.uint16(np.around(circles[0]))

    # Lấy bounding box bao hết các bubble
    xs = [c[0] for c in circles]
    ys = [c[1] for c in circles]

    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    return (x_min, y_min, x_max - x_min, y_max - y_min)
    

# Trả về bounding box (x, y, w, h) của vùng trả lời
# Hoặc None nếu không tìm thấy  
# Ví dụ sử dụng
# box = detect_answer_region("path_to_image.jpg")
# print(box)
# Kết quả: (x, y, w, h) hoặc None
