module.exports = (req, res, next) => {
    if (process.env.DEV_MODE !== 'true') {
        return res.status(403).json({
            error: 'Developer mode is disabled'
        });
    }
    next();
};
