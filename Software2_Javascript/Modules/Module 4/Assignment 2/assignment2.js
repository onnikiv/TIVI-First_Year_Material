const showHaku = document.getElementById("showHaku");
showHaku.addEventListener("submit", async function(event) {
    event.preventDefault();
    const haku = document.getElementById("query").value;
    try {
        const vastaus = await fetch(`https://api.tvmaze.com/search/shows?q=${haku}`);
        const jsonData = await vastaus.json();
        console.log(jsonData);
        jsonData.forEach(item => {
            console.log(item.show.name);
        });
    } catch (error) {
        console.log(error.message);
    }
});
