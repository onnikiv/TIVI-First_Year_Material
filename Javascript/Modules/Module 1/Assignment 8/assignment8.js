const startYear = prompt("Give me a Starting Year:");
const endYear = prompt("Give me an Ending Year:");

const unOrdered = document.querySelector("ul");

// i = alkuvuosi; ehtona (kun) ollaan alle lopetusvuoden, ja sitten lisätään yksi (i),
// listItem = luo li, sitten lisää i:llä saatu vuosi
for (let i = startYear; i < endYear; i++){
    const listItem = document.createElement("li");
    listItem.innerText = i;
    unOrdered.appendChild(listItem);

}
