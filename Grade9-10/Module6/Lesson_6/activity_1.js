
function getHistory() {
    return document.getElementById("history-value").innerText;
}

function printHistory(value) {
    document.getElementById("history-value").innerText = value;
}

function getOutput() {
    return document.getElementById("output-value").innerText;
}

function printOutput(value) {
    if (value == "") {
        document.getElementById("output-value").innerText = value;
    } else {
        document.getElementById("output-value").innerText = formatNumber(value);
    }
}

function formatNumber(value) {
    if (value == "-") {
        return "";
    }

    var num = Number(value);
    return num.toLocaleString("en");
}

function reverseNumberFormat(value) {
    return Number(value.replace(/,/g, ""));
}

var operators = document.getElementsByClassName("operator");

for (var i = 0; i < operators.length; i++) {
    operators[i].addEventListener("click", function () {

        if (this.id == "clear") {
            printHistory("");
            printOutput("");
        }

        else if (this.id == "backspace") {
            var currentOutput = reverseNumberFormat(getOutput()).toString();

            if (currentOutput) {
                currentOutput = currentOutput.substr(0, currentOutput.length - 1);
                printOutput(currentOutput);
            }
        }

        else {
            var output = getOutput();
            var history = getHistory();

            if (output == "" && history != "") {
                if (isNaN(history[history.length - 1])) {
                    history = history.substr(0, history.length - 1);
                }
            }

            if (output != "" || history != "") {
                output = output == "" ? output : reverseNumberFormat(output);
                history = history + output;

                if (this.id == "=") {
                    var answer = eval(history);
                    printOutput(answer);
                    printHistory("");
                }

                else {
                    history = history + this.id;
                    printHistory(history);
                    printOutput("");
                }
            }
        }
    });
}

var numbers = document.getElementsByClassName("number");

for (var i = 0; i < numbers.length; i++) {
    numbers[i].addEventListener("click", function () {

        var output = reverseNumberFormat(getOutput());

        if (output != NaN) {
            output = output + this.id;
            printOutput(output);
        }
    });
}
