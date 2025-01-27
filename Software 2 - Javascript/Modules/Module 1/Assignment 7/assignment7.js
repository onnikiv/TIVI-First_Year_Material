
const howManyDice = parseInt(prompt("How many dice do you want to roll?"));
let sum = 0;
let diceRolls = [];
for (let i = 0; i < howManyDice; i++) {
    let roll = Math.floor(Math.random() * 6) + 1;
    diceRolls.push(roll);
    sum += roll;
}
document.querySelector("p").textContent = `You rolled ${howManyDice} dice: ${diceRolls.join(", ")}. The sum is ${sum}.`;