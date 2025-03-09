let timer;
let remainingTime = 0;
let isRunning = false;
let isPaused = false;
let hours = 0
let minutes = 0
let seconds = 0
let currentHours = 0
let currentMinutes = 0
let currentSeconds = 0

$(document).ready(()=>{
    var timer_input_handler = (event) => {
        let key = (event.keyCode ? event.keyCode : event.which);
        if(key){
            if(key == 8 || key == 13){
                return true
            }
            var val = String.fromCharCode(key)
            if(parseInt(val) == NaN){
                return false;
            }
            minutes = parseInt($("#minutes").val())
            seconds = parseInt($("#seconds").val())
        }
    }

    var max_value_handler = (event) => {
        let key = (event.keyCode ? event.keyCode : event.which);
        if(key){
            if(key == 8 || key == 13){
                return true
            }
            var val = String.fromCharCode(key)
            if(parseInt(val) == NaN){
                return false;
            }
            const new_minutes = parseInt($("#minutes").val())
            const new_seconds = parseInt($("#seconds").val())
            if(new_minutes > 59 || new_seconds > 59){
                $("#minutes").val(minutes)
                $("#seconds").val(seconds)
                return false
            }
        }
    }

    $("#hours").on("keydown", timer_input_handler);
    $("#minutes").on("keydown", timer_input_handler);
    $("#seconds").on("keydown", timer_input_handler);

    $("#minutes").on("keyup", max_value_handler);
    $("#seconds").on("keyup", max_value_handler);
})

function startPauseTimer() {
    if (!isRunning) {
        if (!isPaused){
            hours = parseInt($("#hours").val()) || 0;
            minutes = parseInt($("#minutes").val()) || 0;
            seconds = parseInt($("#seconds").val()) || 0;
        } else {
            hours = currentHours;
            minutes = currentMinutes;
            seconds = currentSeconds;
        }
        remainingTime = (hours * 3600) + (minutes * 60) + seconds;
        
        if (remainingTime > 0) {
            isRunning = true;
            isPaused = false
            document.querySelector('button.btn-primary').innerText = 'Pause';
            countdown();
        }
    } else {
        clearInterval(timer);
        isRunning = false;
        isPaused = true
        currentHours = Math.floor(remainingTime / 3600)
        currentMinutes = Math.floor((remainingTime % 3600) / 60)
        currentSeconds = (remainingTime % 60)
        document.querySelector('button.btn-primary').innerText = 'Start';
    }
}

function countdown() {
    timer = setInterval(() => {
        if (remainingTime > 0) {
            remainingTime--;
            updateDisplay();
        } else {
            clearInterval(timer);
            isRunning = false;
            document.querySelector('button.btn-primary').innerText = 'Start';
        }
    }, 1000);
}

function resetTimer() {
    clearInterval(timer);
    isRunning = false;
    document.querySelector('button.btn-primary').innerText = 'Start';
    hours = parseInt($("#hours").val()) || 0;
    minutes = parseInt($("#minutes").val()) || 0;
    seconds = parseInt($("#seconds").val()) || 0;
    remainingTime = (hours * 3600) + (minutes * 60) + seconds;
    updateDisplay();
}

function updateDisplay() {
    const hrs = Math.floor(remainingTime / 3600).toString().padStart(2, '0');
    const mins = Math.floor((remainingTime % 3600) / 60).toString().padStart(2, '0');
    const secs = (remainingTime % 60).toString().padStart(2, '0');
    document.getElementById('timer').innerText = `${hrs}:${mins}:${secs}`;
}