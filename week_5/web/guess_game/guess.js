const randomNumber =math.floor(math.rndom() * 100 ) +1;
console.log(randomNumber)
let attempt =0;

function checksGuess(){
    const guess = parseInt(document.getElementById("guessfield").value)
    attempt++;
    if(isNaN(guess) || guess < 1 || guess > 100){
        setMessage("please enter a valid number between 1 and 100")
        return;

    }
    if(guess === randomNumber){
        setMessage("Hot air rises")
        document.getElementById("guessField").disabled = true;
    }else if(guess < randomNumber){
        setMessage("Change io view")
    }else(
        setMessage("kam downtown")
    )
}
function setMessage(message){
    document.getElementById("message").textcontent = message
}


