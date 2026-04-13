//print 1 to 5
// for (let count = 1; count <= 5; count++){
// console.log("abhi")}

//Calculate Sum of 1 to 100
/*let sum=0
let n=100;
for(let i=1;i<=n;i++){
    sum=sum+i;
}
console.log("Sum = ",sum)*/

//while loop print  1 to 10
/*let i=1;
while(i <= 10 ){
    console.log(i);
    i++;
}
    */

//do while loop print  1 to 10

/*
let i=1;
do{
    console.log(i);
    i++;
}while(i <= 10)
*/

//for-of loop

// let str = "abhishek";
// let size = 0;
// for(let i of str){
//   console.log("i = ",i)
//     size++;  
// }
// console.log("string size = ",size);

//for-in loop

/*
let student = {
name: "abhishek",
roll: 50,
cgpa:6.2,
};

for (let key in student){
    console.log(key, student[key])
}
    */

//print under 100 even number
/*
for (let i=1;i<=50;i++){
    console.log(i*2)
}
  */

//create a game where you start with any random game number.
//  Ask the user to keep guessing the game number
// until the auser correct value
/*
let gameNum = 24;
let userNum = prompt("Guess the game number : ");
while( userNum != gameNum){
    userNum = prompt("you enter wrong number , Guess again : ");
}
console.log("Congratulations, you entered the right number");
*/

//string 
/*
let str = "abhishek";
let str2 = 'kumar';
console.log(str2.length);
*/

// template letral 
/*
let obj = {
    item: "pen",
    price:10,
    name:"write",
};

let output = `the cost of ${obj.item} is ${obj.price} rupees;`
console.log(output);

console.log("the cost of",obj.item,"is",obj.price,"rupees");

let output = `the cost of is ${1+2+3+5} rupees`;
console.log(output);
*/

//to upercase 
/*
let str = "abhishek";
let newStr = str.toUpperCase();
console.log(str);
console.log(newStr);
*/

//to lowercase
/*
let str = "aASDbhishek";
str = str.toLowerCase();
console.log(str);
*/

//trim
/*
let str = "     abhishek kumar  ";
console.log(str.trim());
*/
 
/*
let fullName = prompt("Enter your full name");
let userName = "@" + fullName + fullName.length;
console.log(userName);
*/

//let fruits = ["Apple","Grapes","Orange"];
//console.log(fruits.length);
// console.log(fruits[2]);

//pop() ,push(), => work from last -- shift(),unshift()=>from start


//let te = "Cybrom";
//let reverseTe = te.split('').reverse().join('');
//console.log(reverseTe);

//looping in array
//let Abhi = ["abhishek","aman","aniket","anshu"]
//let heroes = ["ironman","thar","hulk","abhishek"]
 //for(i=0;i<heroes.length;i++){
   // console.log(heroes[i])
// }

//for of
//for(let abi of Abhi){
 //   console.log(abi);
//}

//calculate average
/*
let ani = [85,97,44,37,76,60]
let s = 0
for(let i of ani){
  s = s + i;
}
let avg = s/ani.length;
console.log(avg)
*/

// teN% discount on every item in array
//let items = [250,645,300,900,50]
//for (let i=0;i<items.length;i++){
   // let offer = items[i]/10;
   // items[i] -= offer;
// }
// console.log(items)

//pop push 

// let fruits = ["apple","banana","orange","Guava"]
// // fruits.push("pine apple","grapes");
// fruits.pop();
// fruits.pop();
// console.log(fruits)

//concat
// let hero = ["amitabh","abhishek","salman"]
// let heroin = ["priyanka","disha"]
// let random = ["company","seeba"]
// let add = hero.concat(heroin,random);
// console.log(add);

//shift() work as delete item like pop from start
//unshift() work as add item like push   from start

//slice(0 to +1)
//splice

// let num = [1,4,5,8,9,6]

// add element
//num.splice(3,0,10)

//remove element
//num.splice(3,1)

//replace element
//num.splice(4,1,102)

// let company = ["Bloomberg","Microsoft","Uber","Google","IBM","Netflix"]

//remove first company from the array
//company.splice(0,1)

//Remove Uber & Add Ola in its place
//company.splice(2,1,"Ola")

//Add amazon at the end
// company.splice("Amazon")

//count vowels 
// function countVowels(str){
//     let count = 0;
//     for(const char of str){
//         if (char === "a" ||
//             char === "e" ||
//             char === "i" ||
//             char === "o" ||
//             char === "u" ) {
//             count++;
//         }
//     }
//     return count;
// }

//count vowels in arrow form
// let countVowel = (str) => {
//      let count = 0;
//      for(const char of str){
//          if (char === "a" ||
//              char === "e" ||
//             char === "i" ||
//             char === "o" ||
//             char === "u" ) {
//             count++;
//         }
//     }
//     return count;
// }

// let n = prompt("Enter a number");
//  let arr = [];

//  for(let i = 1; i <= n; i++){
//     arr[i-1] = i;
//  }
//  console.log(arr);

//  let sum = arr.reduce((res,curr) => {
//     return res+curr;
//  });
//  console.log("sum is",sum);

//  let fact = arr.reduce((res,curr) => {
//     return res*curr;
//  });

//  console.log(fact);
 
// let abhi = document.querySelector('')

//check divisible of 5

// let nums = prompt("Enter a number");

// if(nums%5 === 0){
//   console.log("The number is multiple of 5")
// }else {
//    console.log("The number is not multiple of 5") 
// }
// let str = "acfghrdt";
// console.log(str.toUpperCase());
// console.log(str);

// let arr = [85,97,44,37,76,60];
// let s=0;
// for(let mark of arr){
//  s = s+mark;
 
// }
// console.log(s)

// //ten% discount on every items
// i=0
// let items = [250,645,300,900,50]
// for(let it of items){
//     let offer = it/10;
//     items[i] = items[i]-offer;
//     console.log(items[i])
//     i++;
// }

// let numb = [1,2,3,4,5]
// numb.forEach( function (square)
// {
//     console.log(square*square)
// })

//   let newBtn = document.createElement("button");
//   newBtn.innerText = "click me";

//   newBtn.style.color = "white"
//   newBtn.style.backgroundColor = "red";

//   document.querySelector("body").prepend(newBtn);


