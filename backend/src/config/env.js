require('dotenv').config({ quiet: true }); // tắt log

module.exports = {
    PORT: process.env.PORT || 1206,
    NODE_ENV: process.env.NODE_ENV || 'development',
    DEV_MODE: process.env.DEV_MODE === 'true'
};
