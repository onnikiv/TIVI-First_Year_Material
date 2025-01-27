const vitsiHaku = document.getElementById('vitsiHaku');
vitsiHaku.addEventListener('submit', async function (event) {
    event.preventDefault();
    const haku = document.getElementById('query').value;
    try {
        const vastaus = await fetch(
            `https://api.chucknorris.io/jokes/search?query=${haku}`);
        const jsonData = await vastaus.json();
        
        document.querySelector('article').innerHTML = '';
        
        jsonData.result.forEach((item) => {
            const vitsi = item.value;
            console.log(vitsi);
            
            const paragraphElement = document.createElement('p');
            paragraphElement.textContent = vitsi;
            
            document.querySelector('article').appendChild(paragraphElement);
        });
        
    } catch (error) {
        console.log(error.message);
    }
});
