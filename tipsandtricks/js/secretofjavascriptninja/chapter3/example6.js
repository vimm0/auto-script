// Defines an arrow function
var greet = name => "Greetings " + name;
console.assert(greet("Oishi") === "Greetings Oishi", "Oishi is properly greeted");
var anotherGreet = function (name) {
    return "Greetings " + name;
};
console.assert(anotherGreet("Oishi") === "Greetings Oishi", "Again, Oishi is properly greeted");
