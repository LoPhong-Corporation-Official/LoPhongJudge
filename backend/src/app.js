const express = require('express');
const app = express();

app.use(express.json());

// test route
app.get('/', (req, res) => {
    res.send('Backend is running');
});

app.get('/about', (req, res) => {
    res.send('LoPhong Judge Backend Service\nVersion 1.0.0\nCompany: LoPhong Corporation');
});

app.use('/submit', require('./routes/submit.route'));

// dev route (không crash nếu thiếu)
try {
    if (process.env.DEV_MODE === 'true') {
    app.use('/dev', require('./routes/dev.route'));
    }

} catch (e) {
    console.error('[DEV ROUTE ERROR]', e.message);
}

module.exports = app;
