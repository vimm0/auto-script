#### First-class functions for the novice: definitions and arguments

In JavaScript, objects enjoy certain capabilities:
* They can be created via literals: {}
* They can be assigned to variables, array entries, and properties of other objects:
```
var ninja = {};
ninjaArray.push({});
ninja.data = {};
```
* They can be passed as arguments to functions:
```
function hide(ninja){
ninja.visibility = false;
}
hide({});
```
* They can be returned as values from functions:
```
function returnNewNinja() {
return {};
}
```
* They can possess properties that can be dynamically created and assigned:
```
var ninja = {};
ninja.name = "Hanzo";
```

##### Functions as first-class objects
* Created via literals
```
function ninjaFunction() {}
```
* Assigned to variables, array entries, and properties of other objects
```
var ninjaFunction = function() {};
ninjaArray.push(function(){});
ninja.data = function(){};
```
* Passed as arguments to other functions
```
function call(ninjaFunction){
ninjaFunction();
}
call(function(){});
```
* Returned as values from functions
```
function returnNewNinjaFunction() {
return function(){};
}
```
* They can possess properties that can be dynamically created and assigned:
```
var ninjaFunction = function(){};
ninjaFunction.name = "Hanzo";
```
> Whatever we can do with objects, we can do with functions as well.
##### Fun with functions as objects
```
var ninja = {};
ninja.name = "hitsuke";
var wieldSword = function(){};
wieldSword.swordType = "katana";
```
* Storing functions in a collection
[Example2](./example2.js)
* Memoization
[Example3](./example3.js)

##### Defining functions
* Function declarations and function expressions
[Example4](./example4.js)
[Example5](./example5.js)

```
function myFun(){ return 1;}
```
* Arrow functions (lambda functions)
```
myArg => myArg*2
```
[Example6](./example6.js)

* Function constructors
```
new Function('a', 'b', 'return a + b')
```
* Generator function
```
function* myGen(){ yield 1; }
```
