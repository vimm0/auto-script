// Functions are objects
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw')
    }
} //Circle {radius: 1, draw: ƒ}

const Circle1 = new Function('radius', `
this.radius = radius;
    this.draw = function() {
        console.log('draw')
    }
`
) //{radius: 1, draw: ƒ}

const circle = new Circle1(1); // Circle.call({}, 1) / Circle.apply({}, [1]) 

const another = new Circle(1); // Circle.call({}, 1)
// const another = Circle(1); // Circle.call(window, 1)

