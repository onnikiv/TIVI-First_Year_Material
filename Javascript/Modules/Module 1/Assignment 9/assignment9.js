"use strict";
const primeNumberInput = parseInt(prompt("Give me a Number"));

let isPrimeNumber = primeNumberInput > 1; 
for (let i = 2; i < primeNumberInput; i++) {
    if (primeNumberInput % i === 0) {
        isPrimeNumber = false;
        break;
    }
}

console.log(isPrimeNumber);

const message = isPrimeNumber ? "Prime number: YES" : "Prime number: NO";
document.querySelector("p").textContent += message;
