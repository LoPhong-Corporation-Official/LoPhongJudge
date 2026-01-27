import cv2
from omr import is_filled

cell = cv2.imread(r"D:\LoPhongJudge\backend\ai\example.png")
print(is_filled(cell, debug=True))
# --- IGNORE ---
# File: backend/ai/omr.py
# I moved this file to the correct location.
# test file to ensure everything works fine.