const router = require('express').Router();
const upload = require('../utils/upload.util');
const controller = require('../controllers/submit.controller');

// field name = image
router.post('/', upload.single('image'), controller.submit);

module.exports = router;
