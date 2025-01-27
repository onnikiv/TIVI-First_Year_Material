let kysytytNumerot = [];
const nolla = 0;

while (!kysytytNumerot.includes(nolla)) {
  const luku = parseInt(prompt("Give a Number:   [enter zero to stop]"));
  kysytytNumerot.push(luku);
}

kysytytNumerot.sort(function (a, b) {
  return b - a;
});
console.log(kysytytNumerot);

document.querySelector("p").textContent = kysytytNumerot;
