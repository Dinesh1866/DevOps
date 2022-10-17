//Operators
var a = 10;
var b = 20;

//arithmetic operators
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);
console.log(a % b);
console.log(++a);
console.log(a--);
console.log(a);
console.log(a++);
console.log(a);


//comparison operators
console.log(a == b); //will check only the values are euqal or not eg: 1 and True -> true
console.log(a != b);
console.log(a > b);
console.log(a < b);
console.log(a >= b);
console.log(a <= b);
console.log(a === b); //will check the values and the data types are equal or not eg: 1 and True -> false

//logical operators
console.log(a > 5 && b > 5);
console.log(a > 5 || b > 5);
console.log(!(a > 5 && b > 5));

//ternary operator
console.log(a > 5 ? "a is greater than 5" : "a is less than 5");

//assignment operators
console.log(a += b);
console.log(a -= b);
console.log(a *= b);
console.log(a /= b);
console.log(a %= b);