from omr import read_answers

IMAGE_PATH = r"D:\LoPhongJudge\backend\test\form.png"

answers = read_answers(IMAGE_PATH)

print("KẾT QUẢ NHẬN DẠNG:")
for q, a in answers.items():
    print(f"Câu {q}: {a}")
