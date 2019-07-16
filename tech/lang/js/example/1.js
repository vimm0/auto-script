// if object has one or more method then object is said to have behavior

// Factory function
function createCircle(radius) {
    return {
        radius,
        draw: function(){
            console.log('draw');
        }
    }
}

const circle = createCircle(5)
circle.draw()

// Constructor Function
function Circle(radius){
    // console.log('this ', this)
    this.radius=radius;
    this.draw = function (){
        console.log('draw')
    }
}

const another = new Circle(1);
another.draw()
// new keyword crucial for constructor
// new object create empty object
// set this to point to the object
// return the object

// every object has contructor property and that references the function
// that was used to create an object
let x = {};// javascript engine create equivalent object
// example, another.constructor()
// let x = new Object();
// new String(); for '', ""
// new Boolean(); for true, false
// new Number(); for 1, 2, 3...