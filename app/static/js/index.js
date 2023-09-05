function refresh() {
    var link = "/random_joke";
    fetch(link)
    .then( response => response.json())
    .then(data => 
        {
        document.getElementById('question').innerText = data[0]["question"];
        document.getElementById('answer').innerText = data[0]["answer"];
        console.log(data);
        console.log(data.question)
        }
        )
}