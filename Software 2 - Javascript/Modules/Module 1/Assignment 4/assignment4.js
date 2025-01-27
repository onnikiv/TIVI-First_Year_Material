"use strict";

const nameInput = prompt(`Enter your name: `);
console.log(nameInput);

let randomNumber = Math.floor(Math.random() * 4) + 1;
console.log(randomNumber);
if (nameInput === "Anna") {
  document.querySelector("p").textContent =
    nameInput + ", You are a Ravenclaw!";
} else if (randomNumber === 1) {
  document.querySelector("p").textContent =
    nameInput + ", You are a Gryffindor!";
} else if (randomNumber === 2) {
  document.querySelector("p").textContent =
    nameInput + ", You are a Slytherin!";
} else if (randomNumber === 3) {
  document.querySelector("p").textContent =
    nameInput + ", You are a Hufflepuff!";
} else {
  document.querySelector("p").textContent =
    nameInput + ", You are a Ravenclaw!";
}
