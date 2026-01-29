from pipeline import process_form

IMAGE = r"D:\LoPhongJudge\backend\test\testcase\test2.png"

# ⚠️ chỉnh đúng theo form bạn
SBD_BOX  = (180, 330, 300, 520)
MADE_BOX = (520, 330, 180, 520)

data = process_form(IMAGE, SBD_BOX, MADE_BOX)

print("SBD:", data["sbd"])
print("MÃ ĐỀ:", data["ma_de"])

for k, v in data["answers"].items():
    print(k, v)
