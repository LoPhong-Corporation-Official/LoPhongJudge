const judgeService = require('../services/judge.service');

exports.submit = async (req, res) => {
    try {
        const result = await judgeService.process(req.body);
        res.json(result);
    } catch (e) {
        res.status(500).json({ error: e.message });
    }
};
