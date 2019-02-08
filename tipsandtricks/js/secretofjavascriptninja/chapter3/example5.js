// Function declarations and function expressions
function myFunctionDeclaration() {
    function innerFunction() {
    }
}

var myFunc = function () {
};
myFunc(function () {
    return function () {
    };
});
// Function expression
// as an argument of a
// function call
(function namedFunctionExpression() {})();
+function () {}();
-function () {}();
!function () {}();
~function () {}();
