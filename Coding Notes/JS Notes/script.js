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

