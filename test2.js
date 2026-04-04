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
        alert("Largest number",+l)
        }
    else{
        let s=b
        alert("Largest number",+s)
        }
}
console.log(large());
