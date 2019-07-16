// Abstraction
// Hide details and complexity and show only the essentials
// PROBLEM DOMAIN
// function Circle(radius) {
//     this.radius = radius;
//     this.defaultLocation = {x:0, y:0}
//     this.computeOptimumLocation = function(factor) {
//         // ...
//     }
//     this.draw = function () {
//         this.computeOptimumLocation(0.01)
//         console.log('draw')
//     }
// }

// const circle = new Circle(10);

// Private Properties and Methods

// function Circle(radius) {
//     this.radius = radius;
//     let defaultLocation = {x:0, y:0} // private member
//     // local method / private member (closure)
//     let computeOptimumLocation = function(factor) {
//         // ...
//     }
//     this.draw = function () {
//         computeOptimumLocation(0.01) // (closure)
//         console.log('draw')
//     }
// }

// const circle = new Circle(10);

// Getters/Setters

function Circle(radius) {
    this.radius = radius;
    let defaultLocation = {x:0, y:0}
    this.getDefaultLocation = function() {
        return defaultLocation
    }
    this.draw = function () {
        console.log('draw')
    }

    Object.defineProperty(this, 'defaultLocation', {
        get: function() {
            return defaultLocation
        },
        set: function(value) {
            console.log(value)
            if (!value.x || !value.y)
                throw new Error('Invalid location.')
            defaultLocation = value;
        }
    })
}

const circle = new Circle(10);
// circle.defaultLocation = 10; // throws an error
// circle.defaultLocation = {x : 10, y:10};
console.log(circle.defaultLocation)
// console.log(circle.getDefaultLocation)

circle.draw()