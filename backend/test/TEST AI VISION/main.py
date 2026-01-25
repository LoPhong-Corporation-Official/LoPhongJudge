from detect_answer_region import detect_answer_region

box = detect_answer_region(r"D:\LoPhongJudge\backend\test\VERSION 1\form.png")
print(box)
# Kết quả: (x, y, w, h) hoặc None
# Trả về bounding box (x, y, w, h) của vùng trả lời
# Hoặc None nếu không tìm thấy
