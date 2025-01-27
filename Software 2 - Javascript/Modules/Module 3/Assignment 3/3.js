'use strict';
const names = ['John', 'Paul', 'Jones'];

for (let i = 0; i < names.length; i++) {
    const listItem = document.createElement('li');
    listItem.textContent = names[i];
    document.getElementById('target').appendChild(listItem);
}