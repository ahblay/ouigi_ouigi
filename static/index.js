var alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

$(".upvote").click(cycleUp);

$(".downvote").click(cycleDown);

function cycleUp() {
    console.log("Upvote selected.")
    let currentLetter = $(".letter").text();
    let index = alphabet.indexOf(currentLetter);
    let nextLetter = alphabet[(index - 1) % 26];
    $(".letter").text(nextLetter)
}

function cycleDown() {
    let currentLetter = $(".letter").text();
    let index = alphabet.indexOf(currentLetter);
    let nextLetter = alphabet[(index + 1) % 26];
    $(".letter").text(nextLetter)
}