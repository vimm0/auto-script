// Adding/Removing Properties
function Circle(radius) {
    this.radius = radius;
    this.draw = function() {
        console.log('draw');
    }
}

const circle = new Circle(10);

circle.location = {x:1}

const propertyName = 'center location' // or center-location (useful if property name is more complex, instead of dot notation)
circle[propertyName] = {x:1}

delete circle['location'] // deletes the property name location