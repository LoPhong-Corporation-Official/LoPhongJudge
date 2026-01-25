const multer = require('multer');
const path = require('path');

// lưu file vào /uploads
const storage = multer.diskStorage({
    destination: 'uploads/',
    filename: (req, file, cb) => {
        // đặt tên tránh trùng
        const unique = Date.now() + path.extname(file.originalname);
        cb(null, unique);
    }
});

// chỉ nhận ảnh
const fileFilter = (req, file, cb) => {
    if (!file.mimetype.startsWith('image/')) {
        cb(new Error('Only image allowed'), false);
    }
    cb(null, true);
};

module.exports = multer({ storage, fileFilter });
