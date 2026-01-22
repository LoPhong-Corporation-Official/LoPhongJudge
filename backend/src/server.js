// load env TRƯỚC TẤT CẢ
require('dotenv').config({ quiet: true });

const app = require('./app');

const PORT = process.env.PORT || 1206;

console.log('Starting server...');
console.log(`Environment: ${process.env.NODE_ENV || 'development'}`);
console.log(`Port: ${PORT}`);
app.listen(PORT, () => {
    console.log(`Server started with ${PORT} port`);
});
