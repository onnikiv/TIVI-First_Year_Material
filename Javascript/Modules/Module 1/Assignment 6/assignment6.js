"use strict";

const calculateQuery = confirm("Should I calculate the square root?");
if (calculateQuery) {
    const numberInput = parseInt(prompt(`Enter a number: `));

    if (numberInput < 0) {
        document.querySelector("p").textContent =
            "The square root of a negative number is not defined.";
    } else if (isNaN(numberInput)) {
        document.querySelector("p").textContent = "Please enter a valid number.";
    } else {
        let number = parseInt(numberInput);
        let squareRoot = Math.sqrt(number);
        document.querySelector("p").textContent =
            "The square root of " + number + " is " + squareRoot + ".";
    }
} else {
    document.querySelector("p").textContent =
        "The square root is not calculated.";
}
