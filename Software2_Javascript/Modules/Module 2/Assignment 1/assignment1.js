numbers = [];
console.log(`Listan sisältö aluksi: ${numbers}`);

for (let i = 1; i < 6; i++) {
  const userInput = parseInt(prompt(`${[i]}. Give me a number:`));
  numbers.push(userInput);
  console.log(`${i}. Tapahtuman jälkeen: ${numbers}`);
}
numbers.sort(function (a, b) {
  return b - a;
});

console.log(`Listan sisältö sortattuna takaperin: ${numbers}`);
document.querySelector("p").textContent = `List: ${numbers} `;
