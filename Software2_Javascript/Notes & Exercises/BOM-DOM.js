function locationSuccess(location) {
    console.log('Käyttäjä paikannettu', location);
}

function locationError(error) {
    console.log('paikannus fail', error);
}

const locationOptions = {
    timeout: 5000,
};

// käytetään tapahtumankäsittelijänä, kun p-näppäintä painetaan
function locateUser(event) {
    console.log('Näppäintapahtuma', event);
    if (event.key === 'p') {
        navigator.geolocation.getCurrentPosition(
            locationSuccess,
            locationError,
            locationOptions
        );
    }
}

console.log('Moro!');

// DOM-kikkailua

const section2 = document.querySelectorAll('section')[1];
const pElement = section2.querySelector('p');
pElement.textContent = 'muokattu';

const newP = document.createElement('p');
newP.textContent = 'uusi kappale';
section2.append(newP);
// newP.style = 'color: blue';
newP.classList.add('blue');

const thirdSection = document.querySelector('#third-section');
thirdSection.innerHTML = `
            <h2>Kolmannen osion otsikko</h2>
            <p>
                    Tässä taas tekstiä.
            </p>`;

// Tapahtuman käsittely

const buttonElement = document.querySelector('button');
buttonElement.addEventListener('click', function () {
    // pysäytetään click-eventin eteneminen dom-puussa tähän.
    event.stopPropagation();
    console.log('painettu napulaa');
    // newP.classList.add('red');
    // newP.classList.remove('blue');
    newP.classList.toggle('red');
    newP.classList.toggle('blue');
});

// näppäimistö
document.addEventListener('keypress', locateUser);

// hiiri
`
document.addEventListener('mousemove',(event) => {
    console.log(event);
});
`
// kontekstimenun esto
document.addEventListener('contextmenu', function (event) {
    console.log(event);
    event.preventDefault();
    alert('ei toimi');
})

// tekstikappale klikki
newP.addEventListener('click', function() {
    newP.innerText = 'Klikkasit tähän';
})

// koko dokumentin klikki tapahtuma
document.addEventListener('click', function (event) {
    console.log('sivua klikattu', event);

})

document.addEventListener('click', function (event){
    console.log('sivua klikattu, kohde:', event.target, event.currentTarget.tagName);
    // klikkauksen kohde elementin käsittely
    // event.target.textContent = 'xxx';
    event.target.classList.add('red');
})