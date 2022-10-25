//looping statements
//Looping statements are used to execute a block of statements repeatedly until a particular condition is satisfied.


//for
//for (initialization; condition; increment/decrement) {
//      //code to be executed
//      }

//for loop
for (var i = 0; i < 10; i++) {
      console.log(i);
      }

//for loop with break
for (var i = 0; i < 10; i++) {
      console.log(i);
      if (i == 5) {
            break;
            }
      }

//for loop with continue
for (var i = 0; i < 10; i++) {
      if (i == 5) {
            continue;
            }
      console.log(i);
      }

//while
//while (condition) {
//      //code to be executed
//        counter++;
//      }

//while loop
var i = 0;
while (i < 10) {
      console.log(i);
      i++;
      }

//while loop with break
var i = 0;
while (i < 10) {
      console.log(i);
      if (i == 5) {
            break;
            }
      i++;
      }

//while loop with continue
var i = 0;
while (i < 10) {
      if (i == 5) {
            i++;
            continue;
            }
      console.log(i);
      i++;
      }

//do while
//do {
//      //code to be executed
//      counter++;
//      } while (condition);

//do while loop
var i = 0;
do {
      console.log(i);
      i++;
      }
while (i < 10);

//do while loop with break
var i = 0;
do {
      console.log(i);
      if (i == 5) {
            break;
            }
      i++;
      }
while (i < 10);

//do while loop with continue
var i = 0;
do {
      if (i == 5) {
            i++;
            continue;
            }
      console.log(i);
      i++;
      }
while (i < 10);