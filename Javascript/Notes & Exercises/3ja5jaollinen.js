const luku = parseInt(prompt("Anna luku: "));

const firstParagraphElement = document.querySelector("p");

if (luku % 3 === 0 && luku % 5 === 0) {
  console.log(`${luku} on jaollinen kolmella ja viidellä.`);
  firstParagraphElement.textContent = `${luku} on jaollinen kolmella ja viidellä.`;
} else if (luku % 3 === 0) {
  console.log(`${luku} on jaollinen kolmella.`);
  firstParagraphElement.textContent = `${luku} on jaollinen kolmella.`;
} else if (luku % 5 === 0) {
  console.log(`${luku} on jaollinen viidellä.`);
  firstParagraphElement.textContent = `${luku} on jaollinen viidellä.`;
} else {
  console.log(`${luku} ei ole jaollinen kolmella eikä viidellä.`);
  firstParagraphElement.textContent = `${luku} ei ole jaollinen kolmella eikä viidellä.`;
}
