//example of button click and showing to console
function displayName(elementName) {
    console.log(elementName);
}

//Example of (this)------------------------------------------

// console log "click me"
function example(element) {
    console.log("element clicked", element);
}

//changing button name when clicked 
function turnOff(element) {
    element.innerText = "Off";
}

//hiding a button 

function hide(element) {
    element.remove();
}