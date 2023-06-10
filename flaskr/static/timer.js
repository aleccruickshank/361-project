//import { promptLength } from './play.js';

function startTimer() {

    var currentTime = new Date().getTime();
    var length = parseInt(document.getElementById('prompt').getAttribute("data-length"));

    return [currentTime, length]
};


function endTimer(startTime, mistakes) {
    let finishTime = new Date().getTime()

    let result = finishTime - startTime
    result /= 1000;

    let length = document.getElementById('prompt').getAttribute("data-length");
    let wpm = ((length / 5) - mistakes) / (result / 60)
    let finalWPM = Math.round(wpm)

    let wpmText = document.getElementById('wpm-output')
    let mistakesText = document.getElementById('mistakes-output')

    wpmText.readOnly = false;
    mistakesText.readOnly = false;
    wpmText.value = finalWPM
    mistakesText.value = mistakes
    wpmText.readOnly = true;
    mistakesText.readOnly = true;

    let save = document.getElementById('save').style.visibility = "visible";

}

let saveRaceForm = document.getElementById('save-data');

saveRaceForm.addEventListener("submit", (e) => {

    e.preventDefault();

    let confirmSave = confirm('Are you sure you want to save this score?')

    if (confirmSave == false) {
        return false;
    }

    let outputWpm = document.getElementById('wpm-output')
    let outputMistakes = document.getElementById('mistakes-output')
    let promptId = document.getElementById('prompt-title').getAttribute('data-id')
    let promptTitle = document.getElementById('prompt-title')

    let wpmValue = outputWpm.value;
    let mistakesValue = outputMistakes.value;
    let titleValue = promptTitle.innerText;

    let data = {
        prompt_id: promptId,
        prompt_title: titleValue,
        wpm: wpmValue,
        mistakes: mistakesValue
    }

     // Setup our AJAX request
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/save", true);
    xhttp.setRequestHeader("Content-type", "application/json");

    // Tell our AJAX request how to resolve
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {

            // Clear the output fields

        }
        else if (xhttp.readyState == 4 && xhttp.status != 200) {
            console.log("There was an error with the input.")
        }
    }

    // Send the request and wait for the response
    xhttp.send(JSON.stringify(data));
})

async function saveRace(formData) {
    await fetch('/save', {
        method: 'POST',
        body: formData
    })
}

export { startTimer, endTimer }