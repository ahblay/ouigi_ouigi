var alphabet = ["A", "B", "C", "D", "E", "F", "G",
                "H", "I", "J", "K", "L", "M", "N",
                "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"];
var selectedLetter = "a";
var remainingTime;
var intervalTime = 60000;

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
    $(this).off("click", submit);
    $(this).addClass("disabled");
}

function getTime() {
    $.get("/get_time", function(time) {
        console.log(time);
        remainingTime = (60 - parseInt(time)) * 1000;
        setTimeout(function() {
            getChosenLetter();
            setInterval(getChosenLetter, intervalTime);
        }, remainingTime);
        setTimer();
        setInterval(setTimer, 1000);
    })
}

function getChosenLetter() {
    $.get("/get_chosen_letter", function(letter) {
        console.log(letter)
        new_text = $(".text").text() + letter;
        $(".text").text(new_text);
        $(".submit").on("click", submit);
        $(".submit").removeClass("disabled");
    })
}

function setTimer() {
    remainingTime = remainingTime - 1000;
    let seconds = Math.floor(remainingTime / 1000);
    let minutes = Math.floor(remainingTime / 60000);
    let hours = Math.floor(remainingTime / 3600000);
    let time = ("0" + minutes.toString()).slice(-2) + ":" +
               ("0" + seconds.toString()).slice(-2);
    $(".timer").text(time);
    if (remainingTime <= 0) {
        remainingTime = intervalTime;
    }
}