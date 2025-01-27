let numbers = [];

while (true) {
    const numberInput = parseInt(prompt('Give me a number:  [entering a previously given number stops]'));
    console.log(numberInput);

    if (numbers.includes(numberInput)) {
        console.log(`${numberInput} on jo listassa`);
        break;
    }

    numbers.push(numberInput);
}

numbers.sort();
document.querySelector('p').textContent = numbers;
console.log(numbers);