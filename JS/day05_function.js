//functions
//block of code that can be reused


//function with no return
function greet(){
      console.log("Hello World");
      }

greet();

//function with expression
function add(a,b){
      return a+b;
}
console.log(add(10,20));

//arrow function
var add = (a,b) => a+b;
console.log(add(10,20));

//or
var add = (a,b) =>{ return a+b
      };
console.log(add(10,15));

//function hoisting
console.log(add(10,20));
function add(a,b){
      return a+b;
}

//function scope
var a = 10;
function add(){
      var b = 20;
      console.log(a+b);
}
add();

//function as a parameter
function add(a,b){
      return a+b;
}
function sub(a,b){
      return a-b;
}
function mul(a,b){
      return a*b;
}
function div(a,b){
      return a/b;
}
function calculator(a,b,operator){
      return operator(a,b);
}
console.log(calculator(10,20,add));
console.log(calculator(10,20,sub));
console.log(calculator(10,20,mul));
console.log(calculator(10,20,div));
