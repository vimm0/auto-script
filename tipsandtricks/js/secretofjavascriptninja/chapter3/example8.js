function performAction(ninja, action) {
    return ninja + " " + action;
}

performAction("Fuma", "skulking");
performAction("Yoshi", "skulking");
performAction("Hattori", "skulking");
performAction("Yagyu", "sneaking");

// Tackling default parameters before ES6
function performAction(ninja, action) {
    action = typeof action === "undefined" ? "skulking" : action;
    return ninja + " " + action;
}

console.assert(performAction("Fuma") === "Fuma skulking",
    "The default value is used for Fuma");
console.assert(performAction("Yoshi") === "Yoshi skulking",
    "The default value is used for Yoshi");
console.assert(performAction("Hattori") === "Hattori skulking",
    "The default value is used for Hattori");
// We haven’t passed in a
// second argument, the
// value of the action
// parameter; after executing
// the first function, the body
// statement will default to
// skulking.
console.assert(performAction("Yagyu", "sneaking") === "Yagyu sneaking",
    "Yagyu can do whatever he pleases, even sneak!");

// Tackling default parameters in ES6
function performAction(ninja, action = "skulking") {
    return ninja + " " + action;
}

// In ES6, it’s possible
// to assign a value to a
// function parameter.
console.assert(performAction("Fuma") === "Fuma skulking",
    "The default value is used for Fuma");
console.assert(performAction("Yoshi") === "Yoshi skulking",
    "The default value is used for Yoshi");
// If the value isn’t
// passed in, the default
// value is used.
console.assert(performAction("Hattori") === "Hattori skulking",
    "The default value is used for Hattori");
console.assert(performAction("Yagyu", "sneaking") === "Yagyu sneaking",
    "Yagyu can do whatever he pleases, even sneak!");
