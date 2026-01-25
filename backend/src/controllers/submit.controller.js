exports.submit = async (req, res) => {

    // kiểm tra file
    if (!req.file) {
        return res.status(400).json({
            error: 'Image is required'
        });
    }

    res.json({
        status: 'OK',
        filename: req.file.filename,
        path: req.file.path
    });
};
