const convertToASCII = require('ascii-converter').default;
//allowing for user prompt in node
const prompt = require('prompt-sync')();
//for blinking text effect
const blink = require('../');

blink(function (err, b) {
    console.log(b.version());
});

console.log("Welcome, friend")

convertToASCII('cup1.jfif')
    .then(ascii => console.log(ascii))

    .catch(console.error);


console.log("Hello there, I'm the Pourer.");
console.log("");
// console.log("You are now a guest at my tea-house. Make yourself comfy, you can sit here, at the garden.")
// console.log("You sit outside, at the tea garedn. You hear the birds chirping, and the wind is playing with your hair");
// console.log("After a few minutes, they come back and give you a piece of parchment")
// console.log("With what color will you describe your favorite music gener?")
//color choice - leads to the next question.

//what do you crave? energy, piece and quiet or..? what can I ask about which tea? how do I make it into an expirence, without real tea, just yet? 
//can my game guide people as they drink the tea? what does the Pourer can say to them? how can I make it magical? and witchy?
//I need to relay on my storytelling. How can I write in an engaing way? :O 

console.log("It's seems you are in need for some tea.")
console.log("In order to choose the right tea for you, I need to ask you some questions.");
const season = prompt("What is your favorite season?").toLowerCase();

// if (season == summer){
//     console.log("Your best fit is green tea.")
//     const answer1 = prompt("Are you in need of a recepie?")
// }


if (season == "summer") {
    console.log("Your best fit is green tea.")
}
else if (season == "fall") {
    console.log("Your best fit is black tea.")
}
else if (season == "winter") {
    console.log("Your best fit is herbal tea.")
}
else if (season == "spring") {
    console.log("Your best fit is white tea.")
}

const answer = prompt("Are you in need of a recepie?").toLowerCase();
if (answer == "yes") {
    console.log("enter recepie here");
    // if season == summer call the green tea recepie...etc...
}
else if (answer == "no") {
    console.log("You may come back to ask for a recepie later, then");
}

