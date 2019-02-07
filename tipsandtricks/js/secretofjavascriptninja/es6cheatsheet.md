##### Template literals:  
    `${ninja}`.

##### Block-scoped variables:
```
    let ninja = "Yoshi".
    const ninja = "Yoshi".
```

##### Function parameters:
*Rest parameters*
> The rest parameter syntax allows us to represent an indefinite number of arguments as an array.

```
function multiMax(first, ...remaining){}
multiMax(2, 3, 4, 5); //first: 2;
remaining: [3, 4, 5]
```
    
*Default parameters*
> Default function parameters allow named parameters to be initialized with default values if no value or undefined is passed.
```
function do(ninja, action = "skulk"){ return ninja + " " + action;}
do("Fuma"); //"Fuma skulk"
```

##### Spread operators:
> Spread syntax allows an iterable such as an array expression or string to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected, or an object expression to be expanded in places where zero or more key-value pairs (for object literals) are expected.

```
[...items, 3, 4, 5]
```
