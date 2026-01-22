const pythonService = require('./python.service');
const judgeConfig = require('../config/judge.config');

exports.process = async ({ exam_code, image_base64 }) => {

    // 1. gửi ảnh sang Python OCR
    const ocrResult = await pythonService.run('ocr.py', {
        image_base64
    });

    // 2. nhận diện mã đề
    if (ocrResult.exam_code !== exam_code) {
        return {
            status: 'INVALID',
            reason: 'Wrong exam code'
        };
    }

    // 3. chấm bài
    const score = gradeAnswer(
        ocrResult.answers,
        judgeConfig[exam_code]
    );

    return {
        status: 'OK',
        score,
        detail: ocrResult.answers
    };
};

function gradeAnswer(student, correct) {
    let score = 0;
    for (const q in correct) {
        if (student[q] === correct[q]) score++;
    }
    return score;
}
