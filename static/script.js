$form = $('form').get(0);
timer = 60;
canGuess = true;
$form.onsubmit = async function(evt){
    evt.preventDefault();
    if(canGuess == true){
    console.log('clickled');
    guess = $('#guess').val().toLowerCase();
    check = await checkWord(guess);
    $('#guess').val('');
    console.log(check);
    $('#info').append($(`<li>${guess} is ${check}</li>`));
    console.log($('#info').get(0));
    if (check == "ok")
        $('#score').text(parseInt($('#score').text()) + guess.length)}
}

async function checkWord(word){
    let isValid = await axios.get(`checkWord/${word}`);
    console.log(word);
    lol = isValid.data;
    return lol;
}

function checkTimer(){
    timer--;
    if (timer <= 0){
        canGuess = false;
        $('#timer').text(`Out Of Time`)
        axios.post('/results', {score: $('#score').val()})
    } else{
        $('#timer').text(`Timer: ${timer}`)
        setTimeout(checkTimer, 1000);
    }
}
setTimeout(checkTimer, 1000);
async function getHS(){
    let hs = await axios.get('/gethighscore');
    let what =  hs.data;
    $('#highscore').text(`High Score: ${what}`);
    return what;
}
getHS();
