import sys, json

data = json.loads(sys.stdin.read())

# TODO: OpenCV + OCR thật
result = {
    "exam_code": "A01",
    "answers": {
        "1": "A",
        "2": "B",
        "3": "C"
    }
}

print(json.dumps(result))
