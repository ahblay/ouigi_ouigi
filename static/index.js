var alphabet = ["A", "B", "C", "D", "E", "F", "G",
                "H", "I", "J", "K", "L", "M", "N",
                "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"];
var selectedLetter = "a";
var timer = null;
//var interval = setInterval(getChosenLetter, 5000);

$(getTime);

$(".upvote").click(cycleUp);

$(".downvote").click(cycleDown);

$(".submit").click(submit);

function mod(x, n) {
    result = (x % n + n) % n;
    return result
}

function cycleUp() {
    let currentLetter = $(".letter").text();
    let index = alphabet.indexOf(currentLetter);
    let nextLetter = alphabet[mod((index - 1), 26)];
    $(".letter").text(nextLetter);
    selectedLetter = nextLetter.toLowerCase();
}

function cycleDown() {
    let currentLetter = $(".letter").text();
    let index = alphabet.indexOf(currentLetter);
    let nextLetter = alphabet[mod((index + 1), 26)];
    $(".letter").text(nextLetter);
    selectedLetter = nextLetter.toLowerCase();
}

function submit() {
    $.post("/update_letter", {letter: selectedLetter})
}

function getTime() {
    $.get("/get_time", function(time) {
        console.log(time);
        let remainingTime = (60 - parseInt(time)) * 1000;
        setTimeout(function() {
            setInterval(getChosenLetter, 5000);
        }, remainingTime);
    })
}

function getChosenLetter() {
    $.get("/get_chosen_letter", function(letter) {
        console.log(letter)
        new_text = $(".text").text() + letter
        $(".text").text(new_text)
    })
}