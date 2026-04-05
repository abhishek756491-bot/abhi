// // Q1
// let s = "Javascript"
// //print total number of characters
// console.log(s.length);

// //print script from the same string
// console.log(s.slice(4,10))

// //print full except last word
// console.log(s.slice(0,9))

// //Q2
// let nums = [10,20,30,40,50]

// //remove the first value
// let val = nums.shift()
// console.log(nums)

// let numb = [10,20,30,40,50]
// //Add new value at the beginning
// let Add = numb.unshift(5)
// console.log(numb)

// let number = [10,20,30,40,50]
// //Extract only second value
// let changeNum = number.slice(1,3)
// console.log(changeNum)

// //DElet the the third value from the updted array
// let del3 = number.splice(2,1)
// console.log(number)

// //q3. Using for loop and if-else,print numbers from 1 to 30
// //-if number is even ->print"Even"
// //-if number is odd ->print"Odd"
// for(i=1; i<=30; i++){
//     if(i/2 !== 0 )
//     console.log("Odd")
//     else(i/2 === 0 ) 
//     console.log("Even")
// }

// //Create a button with the label "Show Image". When clicked: If the image is
// //hidden, show it and change button text to "Hide Image
// function toggleImage() {
//             // Get references to the image and button elements
//             var image = document.getElementById("myImage");
//             var button = document.getElementById("toggleButton");

//             // Check the current display style property of the image
//             if (image.style.display === "none") {
//                 // If hidden, show the image and change button text to "Hide Image"
//                 image.style.display = "block";
//                 button.textContent = "Hide Image";
//             } else {
//                 // If visible, hide the image and change button text to "Show Image"
//                 image.style.display = "none";
//                 button.textContent = "Show Image";
//             }
//         }

//method Write a JavaScript program to reverse an array manually (using loop
//  logic only, not using reverse() method). Example: Input [1, 2, 3, 4]
//  Output [4, 3, 2, 1


//  arr = [1,2,3,4]
//  arr1 = []
// for(let i=arr.length-1; i >= 0; i--){
//     arr1.push(arr[i]);
// }
// console.log(arr1)



//Q1. Even or Odd Check

let even=()=>{
    let number=prompt("Enter your choice number")
    if(number%2===0)
        alert("Even")
    else
        alert("Odd")
}

//2. Positive, Negative Number or zero

let math=()=>{
let num=prompt("Enter your choice number")
if (num>0)
    alert("positive number")
else if(num<0)
    alert("negative number")
else
    alert("0")

}


//


//Q3. Voting Eligibility

let vote=()=>{
    let i=prompt("Enter your age for vote")
    
    if ( i>=18)
        alert("you can eligible for vote")
    else
        alert("you can eligible for vote")
}

//Q4. Largest of Two Numbers

let large=()=>{
    let a=prompt("Enter first number")
    let b=prompt("Enter second number")
    if ( a>b){
        let l=a;
        alert("Largest number = "+l)
        }
    else{
        let s=b
        alert("Largest number = "+s)
        }
}
// console.log(large());


//Q5. Pass or Fail System
let num=()=>{
//Ask user to enter marks.
let marks=prompt("Enter marks: ")

//If marks are greater than or equal to 40 → Pass, otherwise Fail.
if(marks>=40)
    alert("Pass")

//Display result using alert.
 else
    alert("fail")
}
// console.log(num())

 //Q6. Grade System

let number=()=>{
//Take marks as input.
let mark=prompt("Enter marks under 100 : ")

//Use multiple else if conditions to assign grades:
//90+ → A, 70–89 → B, 50–69 → C, below 50 → Fail.
//Display grade.
if(mark>=90)
    alert("A")
else if(70<=mark || mark>90)
    alert("B")
else if(mark>=50 || mark<=69)
    alert("C")
else if(mark<50)
    alert("Fail")
}
// console.log(number())

//Q7. Largest of Three Numbers

let checkthree=()=>{
//Take three numbers from the user.
let k=prompt("Enter first number")
let l=prompt("Enter Second number")
let m=prompt("Enter THird number")

//Find and display the largest among them using if-else if.
if(k>=l && k>=m){
    let p=k;
    alert("largest number = "+p)
    }
else if(l>=m && l>=k){
    p=l;
    alert("largest number = "+p)
    }
else {
    p=m;
    alert("largest number = "+p)
}
}
// console.log(checkthree())

//Q8. Leap Year Check

let year=()=>{
//Ask user to enter a year.
let y=prompt("Enter number of year")

//Check whether it is a leap year or not using conditions.
if (y%4==0 && y%100!=0 || y%400==0)
    alert("it is leap year")
else
    alert("it is not leap year")
}
// console.log(year())

//Q9. Character Type Checker
let char=()=>{
//Take a single character input.
let chara=prompt("Enter single char")

//Check whether it is a digit, alphabet, or special character.
if(chara == "a-b")
     alert("it is a alphabate");
else if(chara == "1-9" ||"0")
     alert("it is a digit");
else 
    alert("it is special character")
}
// console.log(char())

//Q10. Simple Calculator

let operator=()=>{
    //Take two numbers and one operator (+, -, *, /) from the user.
    let k=parseInt(prompt("Enter first number"))
    let l=parseInt(prompt("Enter Second number"))
    let operate=prompt("+,-,*,/")

    //Perform the operation based on the operator using if-else if.
    if(operate == '+')
        alert(k+l)
    else if(operate == '-')
        alert(k-l)
    else if(operate == '*')
        alert(k*l)
    else if(operate == '/')
        alert(k/l)
}
// console.log(operator())

//Q11. Print Numbers 1 to N

let printN=()=>{

//Take a number n from the user.
let N=parseInt(prompt("Enter number"))

//se a for loop to print numbers from 1 to n.
for(let i=1;i<=N;i++)
    console.log(i)
}
// console.log(printN())

//Q12. Sum of First N Numbers

let sum=()=>{

//Ask user for a number n.
let n=parseInt(prompt("Enter your choice number"))

//Use a loop to calculate sum from 1 to n.
let sum=0;
let a=0
while(a<=n){
    sum=sum+a;
   console.log("sum is = "+sum);
   a++;
}
}
// console.log(sum());

//Q13. Multiplication Table

let table=()=>{

//Take a number from user.
let t=parseInt(prompt("Enter your choice number for table"))

//Print its multiplication table from 1 to 10 using loop.

 a=1
 while(a<=10)
    table=t*a
    console.log("Table is ",+table)
}
// console.log(table())


//Q14. Factorial of a Number
let fact=()=>{

//Take a number from the user.
let n=prompt("Enter your choice number")

//Use loop to calculate factorial of that number.
a=1;
f=1;
while (a<=n){
   f=f*a;
  console.log(f);
  a++;
  }
}
// console.log(fact())

//Q15. Count Digits in a Number

// let count=()=>{
// //Take a number input.
// let n=prompt("Enter your choice number")

// //Use loop to count how many digits are present.
// let count=0;
// while (n%10)
//     count++
//   alert(count)
// }
// // console.log(count())

//Q16. Print Even Numbers
let evenN=()=>{

//Take a number n.
let n=prompt("Enter your choice number")

//Use loop and condition to print all even numbers from 1 to n.
a=2
while (a<=n){
    if (a%2==0)
      console.log(+a);
    a++
}
}
// console.log(evenN())

//Q17. Sum of Even Numbers
let sumNeven=()=>{

//Take input n.
let n=prompt("Enter your choice number for sumeven")

//Find the sum of all even numbers between 1 and n.
sum=0
a=2
while (a<=n){
    if (a%2==0)
        sum = sum+a;
      console.log(sum);
    a++
}
}
// console.log(sumNeven(sum));

//Q18. Prime Number Check
let prime=()=>{

//Take a number from user.
let n=prompt("Enter your choice number for prime ")

//Use loop and condition to check whether it is prime or not.

}