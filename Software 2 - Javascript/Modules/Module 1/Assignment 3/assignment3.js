"use strict";
// Numero promptit. Promptit muutetaan integereiksi.
const number = parseInt(prompt(`1. Enter a number: `));
const number2 = parseInt(prompt(`2. Enter another number: `));
const number3 = parseInt(prompt(`3. Enter a third number: `));

// Summa, tulo ja keskiarvo muunnokset.
let sum = number + number2 + number3;
let product = number * number2 * number3;
let average = sum / 3;

// Viittaukset div-elementteihin, <div id="sum"></div> tyyppisesti, querySelectorissa pitää muistaa # merkki.
const sumElement = document.querySelector("#sum");
console.log(sumElement); // Debug consoleen
sumElement.textContent = "The Sum of your numbers is " + sum + ".";

const productElement = document.querySelector("#product");
console.log(productElement); // Debug consoleen
productElement.textContent = "The Product of your numbers is " + product + ".";

const averageElement = document.querySelector("#average");
console.log(averageElement); // Debug consoleen
averageElement.textContent = "The Average of your numbers is " + average + ".";
