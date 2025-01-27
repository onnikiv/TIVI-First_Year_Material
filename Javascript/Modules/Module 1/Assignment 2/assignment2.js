'use strict';
const name = prompt('Give me your name:');
console.log(`Hello, ${name}!`);

document.querySelector('p').textContent = `Hello, ${name}!`;
