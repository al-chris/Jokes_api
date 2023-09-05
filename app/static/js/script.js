// JavaScript for Jokes API webpage

const reselectButton = document.getElementById('reselect-button');
const createButton = document.getElementById('create-button');
const modal = document.getElementById('modal');
const closeButton = document.getElementById('close-button');
const jokeForm = document.getElementById('joke-form');
const jokeQuestion = document.getElementById('joke-question');
const jokeResponse = document.getElementById('joke-response');
const jokeTitle = document.querySelector('.joke-title');
const jokeResponseElement = document.querySelector('.joke-response');

// Function to toggle the theme
function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode'); // Toggle the 'dark-mode' class on the body
}

// Event listener for toggling light/dark mode
const themeSwitch = document.getElementById('theme-switch');
themeSwitch.addEventListener('change', toggleTheme);


// Event listener for opening the modal
createButton.addEventListener('click', () => {
    modal.style.display = 'block';
});

// Event listener for closing the modal
closeButton.addEventListener('click', () => {
    modal.style.display = 'none';
    jokeForm.reset();
});

// Event listener for submitting the joke form
jokeForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const question = jokeQuestion.value;
    const response = jokeResponse.value;

    if (question && response) {
        jokeTitle.textContent = question;
        jokeResponseElement.textContent = response;
        modal.style.display = 'none';
        jokeForm.reset();
    }
});

// Event listener for reselecting jokes
reselectButton.addEventListener('click', () => {
    // Add logic to fetch jokes from an API and display them
    // For example, you can use the Fetch API to make a request
    // Update the jokeTitle and jokeResponseElement accordingly
    var link = "/random_joke";
    fetch(link)
    .then( response => response.json())
    .then(data => 
        {
        document.getElementById('joke-title').innerText = data[0]["question"];
        document.getElementById('joke-response').innerText = data[0]["answer"];
        console.log(data);
        console.log(data.question)
        }
        )
});
