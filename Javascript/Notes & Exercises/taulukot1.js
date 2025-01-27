// JS mod 2 - taulukot

const names = [];
// Alkioon viittaaminen indeksin avulla
names[0] = 'Aku';
names[1] = 'Iines';

console.log(names[2]);

// Taulukon loppuun lisääminen
names.push('Hannu');
console.log(names);

// Taulukkon viimeisen arvon poistaminen
const lastName = names.pop();
console.log(names);
console.log(lastName);
names.unshift('Minni');

const ages = [4, 55, 36, 'kuusi'];
// console.log(ages.length);

for (let i = 0; i < ages.length; i++) {
    console.log(ages[i], names[i]);
}
console.log('-');
// Taulukko tulostus taaksepäin
for (let i = ages.length-1; i >= 0; i--) {
    console.log(ages[i], names[i]);
}

// samaten kun pythonissa for i in range()
for (const name of names) {
    console.log('Nimi: ' + name);
}

ages.reverse();
console.log(ages);

// arvon etsiminen taulukosta
const searchParam = 'Akusdf';
if (names.includes(searchParam)) {
    console.log(searchParam + ' löytyi.');
    // katsotaan missä kohtaa taulukko löydetty alkion arvo on
    console.log(names.IndexOf(searchParam));   
} else{
    console.log(searchParam + ' ei löytynyt.');
}

// taulukon järjestäminen aakkosjärjestykseen
ages.sort();
console.log(ages);

// pienimmästä numeerisesta arvosta suurimpaan
ages.sort((a, b) => a-b);
console.log(ages);

const person1 = {
    age: 76,
    name: 'Roope',
};
const person2 = {
    name: 'Aku',
    age: 55,
};
person2.lastName = 'Ankka';
person2.name = 'Donald';
console.log(person1, person2);
delete person2.lastName;
console.log(person1, person2);

// sijoitetaan oliot taulukkoon
const persons = [person1, person2];
persons.push({name: names[0], age: ages[0]});
console.log(persons);

// viittaaminen ominaisuksiin 
for (const person of persons) {
    console.log(`Nimi: ${person.name}, ${person.age['age']} v.`);
}