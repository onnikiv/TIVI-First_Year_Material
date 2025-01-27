// Shift+ALT+F to format the code
// Sääntö 1. -- AVAA KEHITYSTYÖKALUT

"use strict"; // Koodin suoritus vaativaksi

console.log("I have awaken!");

const name = "Onni";
const names = ["Aku", "Iines", "Heluna"];

// javascriptissä pitää esitellä muuttujat ennen käyttöä
let age, height;
age = 5.1;
console.log(age, typeof age, height, typeof height);

// muutetaan number -> string
age = age.toString();
console.log(age);

// muutetaan string -> number
// age = parseInt(age); // ottaa vain kokonaisluvun
age = parseFloat(age);
console.log(age, typeof age);
const ageAdd = 3;
console.log(age + ageAdd);

// lisätään arvoon 1 // kaikki tekee saman
age++;
age = age + 1;
age += 1;

console.log(`${name}:n ikä on ${age + 1} vuotta.`);

const isUnderAge = true;
console.log(isUnderAge, typeof isUnderAge);

// printti
console.log("Moro " + name + "!");
console.log("Tulostetaan kaikki nimet:", name, names);

// alert("Moro " + name);

// alert('Toinen alertti');

// haetaan viittaus ensimmäiseen p-elementtiin
const firstParagraphElement = document.querySelector("p");
console.log(firstParagraphElement);
// muutetaan p-elementin tekstisisältöä
firstParagraphElement.textContent = "Moro " + name;

const allParagraphElements = document.querySelectorAll("p");
console.log(allParagraphElements);
allParagraphElements[2].textContent = "Hihii";

// syötteen lukeminen suoraan JS
// const name1 = prompt("Anna nimi:");
// console.log(name1);

// Math
console.log(Math.random());

// arvotaan kokonaislukuna arvo väliltä 1-6
console.log(Math.floor(Math.random()*6+1));