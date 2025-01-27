fetch(`https://api.chucknorris.io/jokes/random`)
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        console.log(data.value);
    })
