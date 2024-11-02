document.addEventListener('DOMContentLoaded', () => {
    const diceContainer = document.getElementById('dice-container');
    const rollButton = document.getElementById('roll-button');
    const endTurnButton = document.getElementById('end-turn-button');
    const scoreElements = {
        ones: document.getElementById('score-ones'),
        twos: document.getElementById('score-twos'),
        threes: document.getElementById('score-threes'),
        total: document.getElementById('total-score')
    };

    let diceValues = [1, 2, 3, 4, 5]; // Initial dice values
    let rollCount = 0;

    async function rollDice() {
        try {
            const response = await fetch('/roll-dices');
            if (!response.ok) throw new Error('Failed to fetch dice values');
            const diceValues = await response.json();

            // Update the dice values on the UI
            const diceContainer = document.getElementById('dice-container');
            diceValues.forEach((value, index) => {
                diceContainer.children[index].textContent = value;
            });
            rollCount++;
        } catch (error) {
            console.error(error);
            alert('Error rolling dice. Please try again.');
        }
    }


    function resetRollCount() {
        rollCount = 0;
    }

    function calculateScore() {
        // Example calculation for Ones, Twos, and Threes
        let onesScore = diceValues.filter(value => value === 1).length * 1;
        let twosScore = diceValues.filter(value => value === 2).length * 2;
        let threesScore = diceValues.filter(value => value === 3).length * 3;

        // Update individual scores on the scorecard
        scoreElements.ones.textContent = onesScore;
        scoreElements.twos.textContent = twosScore;
        scoreElements.threes.textContent = threesScore;

        // Calculate and update total score
        let totalScore = onesScore + twosScore + threesScore;
        scoreElements.total.textContent = totalScore;
    }

    rollButton.addEventListener('click', rollDice);

    endTurnButton.addEventListener('click', () => {
        calculateScore();
        resetRollCount();
        alert('End of turn. Your score has been updated.');
    });

    Array.from(diceContainer.children).forEach(die => {
        die.addEventListener('click', () => {
            die.classList.toggle('keep');
            die.style.backgroundColor = die.classList.contains('keep') ? '#d3d3d3' : '#fff';
        });
    });
});
