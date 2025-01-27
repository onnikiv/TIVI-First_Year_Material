const listElement = document.getElementById('target');

const listItem1 = document.createElement('li');
const listItem2 = document.createElement('li');
const listItem3 = document.createElement('li');

listItem1.textContent = 'First item';
listItem2.textContent = 'Second item';
listItem3.textContent = 'Third item';

listElement.appendChild(listItem1);
listElement.appendChild(listItem2);
listElement.appendChild(listItem3);

listItem2.classList.add('my-item');
