"use strict";

const yearInput = prompt(`Enter a year: `);
console.log(yearInput);
let year = parseInt(yearInput);
console.log(year);
if (year % 4 === 0 && year % 100 !== 0) {
  document.querySelector("p").textContent = year + " is a leap year!";
} else if (year % 400 === 0) {
  document.querySelector("p").textContent = year + " is a leap year!";
} else {
  document.querySelector("p").textContent = year + " is not a leap year!";
}
