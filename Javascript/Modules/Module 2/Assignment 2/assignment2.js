const userInput = parseInt(prompt("Give me the number of participants:"));

const nameList = [];
for (let i = 1; i <= userInput; i++) {
  const nameInput = prompt(`${i}. Participant's name:`);
  nameList.push(nameInput);
}

console.log(nameList);

const sortedNameList = nameList.sort();
console.log(sortedNameList);

const unorderedList = document.createElement("ul");
document.body.appendChild(unorderedList);

sortedNameList.forEach((name) => {
  const listItem = document.createElement("li");
  listItem.textContent = name;
  unorderedList.appendChild(listItem);
});
