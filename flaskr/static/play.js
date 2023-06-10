import { startTimer, endTimer } from './timer.js';

// Calls partner's microservice to GET random prompt
async function getPrompt(URL) {
  await fetch(URL)
  .then((response) => response.json())
  .then((quote) => {

    let promptText = document.getElementById('prompt');
    promptText.setAttribute("data-length", quote.prompt.length)
    let promptTitle = document.getElementById('prompt-title')
    promptTitle.setAttribute("data-id", quote.id)

//  Add title to webpage
    let title = document.createElement('h2')
    title.innerText = quote.title
    promptTitle.appendChild(title)

//  Assign each individual character to a span
    quote.prompt.split('').forEach(letter => {
        const letterSpan = document.createElement('span')
        letterSpan.innerText = letter
        promptText.appendChild(letterSpan)
    })

  });
};


// Generate random prompt
let URL = "http://localhost:5213/prompts/";
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

getPrompt(URL + String(getRandomInt(10)));

const promptInput = document.getElementById('prompt-input')
const promptText = document.getElementById('prompt');
let begin = true

// Handles text entry field correctness, begins WPM count
var startTime;
promptInput.addEventListener('input', () => {

    if (promptInput.value.length == 1 && begin == true) {
        startTime = startTimer()
        begin = false
    }
    const arrPrompt = promptText.querySelectorAll('span')
    const arrValue = promptInput.value.split('')

    let correct = true

    if (arrValue.length == arrPrompt.length) {
        let mistakes = promptText.querySelectorAll(".incorrect").length
        endTimer(startTime[0], mistakes)
    }

    arrPrompt.forEach((letterSpan, index) => {
        const letter = arrValue[index]

        if (letter == null) {
            letterSpan.classList.remove('correct')
            letterSpan.classList.remove('incorrect')

        } else if (letter === letterSpan.innerText) {
            letterSpan.classList.add('correct')
            letterSpan.classList.remove('incorrect')

        } else {
            letterSpan.classList.add('incorrect')
            letterSpan.classList.remove('correct')
            correct = false

        }

    })

});

