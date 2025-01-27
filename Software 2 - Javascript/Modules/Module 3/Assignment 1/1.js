const listElement = document.getElementById("target");

const listItems = `
<li>First item</li>
<li>Second item</li>
<li>Third item</li>`;

listElement.innerHTML = listItems;
listElement.classList.add("my-list");
