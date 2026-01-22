const router = require('express').Router();
const devOnly = require('../middlewares/dev.middleware');

router.get('/', devOnly, (req, res) => {
    res.json({ status: 'DEV ROOT OK' });
});

router.get('/ping', devOnly, (req, res) => {
    res.json({ status: 'DEV OK' });
});

module.exports = router;
// Compare this snippet from backend/src/config/env.js:
// require('dotenv').config();
// 
// module.exports = {
//     PORT: process.env.PORT || 3000,
//     NODE_ENV: process.env.NODE_ENV || 'development