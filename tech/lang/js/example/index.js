let baseSalary = 30000;
let overtime = 10;
let rate = 20;

// procedural
function getWage(baseSalary, overtime, rate) {
    return baseSalary + (overtime * rate)
}
console.log(getWage(baseSalary, overtime, rate))
// Encapsulation
// reduce complexity
// increase reusability
let employee = {
    baseSalary: 30000,
    overtime: 10,
    rate: 20,
    getWage: function () {
        return this.baseSalary + (this.overtime * this.rate)
    }
};
// the best functions are those with no parameters
console.log(employee.getWage());

// Abstraction
// Simpler Interface
// Reduce the impact of change

// Inheritance
// helps to reduce redundant code

// Polymorphism
// refactor switch/case statements

console.log("hellow world")