// Value vs Reference Types
// Primitives are copied by their value
// Objects are copied by their reference

// let x = 10;
// let y = x; // copies real value
// x = 20;

let x = {value: 10}
let y = x; // copies address in memory (objects are always passed by reference)

x.value = 20

// let number = 10
// function increase(number){
//     number++;
// }

// increase(number)
// console.log(number)

let obj = {value: 10}

function increase (obj) {
    obj.value++;
}

increase(obj)
console.log(obj)