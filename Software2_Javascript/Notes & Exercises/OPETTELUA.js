'use strict';

function ympyräLaskuri () {
  const säde = parseFloat(prompt('anna ympyrän säde'));
  const pintaAla = Math.PI * Math.pow(säde,2);
  const pintalaPyöristettynä = pintaAla.toFixed(2)
  document.querySelector('p').textContent = `Ympyrän pinta-ala on: ${pintalaPyöristettynä}`;
}

function kysytään() {
  const kyssäri = confirm("Haluatko laskea ympyrrän pinta-alan?");
  if (kyssäri === true) {
  ympyräLaskuri();
  } else {
    alert("Suce ma Bit");
  }
}

kysytään();


