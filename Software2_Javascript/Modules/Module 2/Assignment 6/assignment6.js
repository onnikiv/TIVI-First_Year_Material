function diceRoll() {
    return Math.ceil(Math.random() * 6);
}

function main() {
    while (true) {
        let roll = diceRoll();
        console.log(roll);

        const createListItem = document.createElement('li');
        createListItem.textContent = roll;
        document.querySelector('ul').appendChild(createListItem);

        if (roll === 6) {
            break;
        }
    }
}

main();
