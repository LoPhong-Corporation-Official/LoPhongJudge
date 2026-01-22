const router = require('express').Router();

// health check
router.get('/', (req, res) => {
    res.send('Backend is running');
});

module.exports = router;
