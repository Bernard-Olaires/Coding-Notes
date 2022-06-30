//example of button click and showing to console (23-34)
function displayName(elementName) {
    console.log(elementName);
}

// console log "click me" (39-41)
function example(element) {
    console.log("element clicked", element);
}

//changing button name when clicked (46-48)
function turnOff(element) {
    element.innerText = "Off";
}

//hiding a button (53)

function hide(element) {
    element.remove();
}

//hover (58-63)

function addShadow(element) {
    element.classList.add("shadow");
}

function removeShadow(element) {
    element.classList.remove("shadow");
}


//hoover continued (66-67)

function over(element) {
    alert("mouseover");
}

function out(element) {
    alert("mouseout")
}

// QuerySelector (70-72)

var count = 1;
var countElement = document.querySelector("#count");

console.log(countElement);

function add1() {
    count++;
    countElement.innerText = "the count is " + count;
    console.log(count);
}

function subtract1() {
    count--;
    countElement.innerText = "the count is " + count;
    console.log(count);
}

//changing html and css (75-)

var animalImg = document.querySelector("#animal");

console.log(animalImg);

function pickCat(element) {
    element.style.backgroundColor = "goldenrod" ;
    animalImg.src = "./img/cat.jpg";
    console.log(animalImg.src);
}

function pickDog(element) {
    element.classList.add("btn");
    animalImg.src = "./img/dog.jpg"
    console.log(animalImg.src);
}


// boolean notes

// a ==  b: true if a is equal to b (ex. 9 = 9)
// a != b: true if a is not equal to b (ex. 9 = 10)
// a < b: true if a is less than b (ex. 9 < 12)
// a > b: true if a is greater than b (ex. 9 > 8)
// a <= b: true if a is less than or equal to b (ex. 9 < 12 or 9 = 9)
// a >= b: true if a is greater than or equal to b (ex 9 >8 or 9 = 9)


var isSunny = true;
var isRaining = false;
    
if(isSunny) {
    console.log("Wear sunscreen");
}
    
if(isRaining) {
    console.log("Bring an umbrella");
}

if(isSunny == true) {
    console.log("Also wear a hat");
}


// boolean notes (else and if)

var today = new Date();
if(today.getDay() == 1) {
    console.log("I hate Mondays!");
}
    
if(today.getDay() != 1) {
    console.log("Today is alright!");
}

// using else to avoid wirting second condition

var today = new Date();
if(today.getDay() == 3) {
    console.log("I hate Mondays!");
} else {
    console.log("Today is alright!");
}

// adding else if 

var today = new Date();
if(today.getDay() == 5) {
    console.log("I hate Mondays!");
} else if(today.getDay() == 5) {
    console.log("Friday? More like Fri-yay!");
} else {
    console.log("Today is alright!");
}


// multiple conditions 

var temperature = 60; // let's assume this is degrees Fahrenheit
var isRaining = false;
    
if(temperature >= 50) {
    if(!isRaining) {
        console.log("This is a good day to go for a walk!");
    }
}


// can be written in a simpler way:

var temperature = 60; // let's assume this is degrees Fahrenheit
var isRaining = false;
    
if(temperature >= 50 && !isRaining) {
    console.log("This is a good day to go for a walk!");
}

// a && b : true if both a and b are ture 
// a || b : true if either a or b is true


// Modulo Operator 

var is5even = 5 % 2 == 0;
var is500even = 500 % 2 == 0;
    
console.log(is5even);   // false
console.log(is500even); // true


var is78DivisibleBy3 = 78 % 3 == 0;
console.log(is78DivisibleBy3); // true

// loops

for(var i=0; i<3; i++) {
    console.log(i);
}

for(var i=10; i>0; i--) {
    console.log(i);
}


for(var i=12; i>3; i-=2) {
    console.log(i);
}
// this will print 12, 10, 8, 6, 4
    
for(var i=0.25; i<3; i+=0.5) {
    console.log(i);
}
// this will print 0.25, 0.75, 1.25, 1.75, 2.25, 2.75

// types of loops 

// while loop:

for(var i=0; i<3; i++) {
    console.log(i);
}
    
var i = 0;
while(i<3) {
    console.log(i);
    i++;
}

// continued:

var start = 0;
var end = 10;
    
while(start <= end) {
    console.log("start: " + start + ", end: " + end);
    start++;
    end--;
}

// practice
console.log(8%3)