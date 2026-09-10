var selection = prompt("Welcome to Shape Calculator. \n Select your option. \n1. Rectangle. \n2. Triangle. \n3. Circle. \n4. Parallelogram");

if (selection == '1') {
    var lengthValue = prompt('Please enter the length')
    var widthValue = prompt('Please enter the width')
    var answer = Number(lengthValue) * Number(widthValue)
    alert('The calculated area is ' + answer)
}

if (selection == '2') {
    var heightValue = prompt('Please enter the height')
    var baseValue = prompt('Please enter the base')
    var answer = Number(heightValue) * Number(baseValue) / 2
    alert('The calculated area is ' + answer)
}

if (selection == '3') {
    var radiusValue = prompt('Please enter the radius')
    var answer = 3.14 * Number(radiusValue) * Number(radiusValue)
    alert('The calculated area is ' + answer)
}

if (selection == '4') {
    var heightValue = prompt('Please enter the height')
    var baseValue = prompt('Please enter the corresponding base')
    var answer = Number(heightValue) * Number(baseValue)
    alert('The calculated area is ' + answer)
}