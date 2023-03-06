const APILINK = '';
const IMG_PATH = '';
const SEARCHAPI = '';

const main = document.getElementById("section");
const form = document.getElementById("form");
const search = document.getElementById("query");

returnMovies(APILINK)
function returnMovies(url){
    fetch(url).then(res => res.json())
    .then(function(data)){
        console.log(data.results);
        data.results.forEach(element => {
            const div_card = document.createElement('div');
        });
        
    });
}