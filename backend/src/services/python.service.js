const { spawn } = require('child_process');
const path = require('path');

exports.run = (script, payload) => {
    return new Promise((resolve, reject) => {

        const py = spawn('python', [
            path.join(__dirname, `../../ai/${script}`)
        ]);

        let out = '';
        let err = '';

        py.stdout.on('data', d => out += d.toString());
        py.stderr.on('data', d => err += d.toString());

        py.on('close', () => {
            if (err) return reject(new Error(err));
            resolve(JSON.parse(out));
        });

        py.stdin.write(JSON.stringify(payload));
        py.stdin.end();
    });
};
