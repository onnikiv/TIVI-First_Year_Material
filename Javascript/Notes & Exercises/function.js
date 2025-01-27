// JS Mod 2 - funktiot

// Periteinen funktion määritelmä
function doSomething() {
  console.log("doing something");
}
doSomething();

const doSomethingMore = function () {
  console.log("doing something else");
};

const result = doSomethingMore();
console.log(result)

const ages = [4, 55, 36];

// Vertailu funktio sort()- metodia varten
function compare(val1, val2) {
    return val1 - val2;
}
console.log(compare(4, 33));
// ages.sort(compare);

// vertailu funktio nimettömänä funktiona
ages.sort(function (val1, val2) {
        return val1 - val2;
});
// vertailu funktio nuolifunktiona
ages.sort((val1, val2) => val1 -val2);
console.log(ages)


function logArray(array) {
    const ages = []
    console.log(ages);
    console.log(array);
}
logArray(ages);