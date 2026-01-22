const router = require('express').Router();
const controller = require('../controllers/submit.controller');

router.post('/', controller.submit);

module.exports = router;
