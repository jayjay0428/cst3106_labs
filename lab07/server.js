const express = require('express');
const app = express();
const PORT = 3000;

// Middleware to serve static files
app.use(express.static('public'));

// Endpoint to roll the dice
app.get('/roll-dices', (req, res) => {
    const diceValues = Array.from({ length: 5 }, () => Math.floor(Math.random() * 6) + 1);
    res.json(diceValues);
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
