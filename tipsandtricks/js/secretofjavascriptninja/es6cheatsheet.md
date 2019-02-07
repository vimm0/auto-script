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

##### Arrow Function
> An arrow function expression is a syntactically compact alternative to a regular function expression, although without its own bindings to the this, arguments, super, or new.target keywords. Arrow function expressions are ill suited as methods, and they cannot be used as constructors.

```
const values = [0, 3, 2, 5, 7, 4, 8, 1];
values.sort((v1,v2) => v1 - v2); /*OR*/ values.sort((v1,v2) => { return v1 - v2;});
value.forEach(value => console.log(value));
```

##### Generators
> The Generator object is returned by a generator function and it conforms to both the iterable protocol and the iterator protocol.

```
function *IdGenerator(){
 let id = 0;
 while(true){ yield ++id; }
}
```

##### Promises
> The Promise object represents the eventual completion (or failure) of an asynchronous operation, and its resulting value.

```
 new Promise((resolve, reject) => {});.
 myPromise.then(val => console.log("Success"), err => console.log("Error"));
 myPromise.catch(e => alert(e));.
```
