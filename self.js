let oddEven=()=>{
    let num=prompt("Enter a number")
    if(num%2==0){
        alert("Even")
    }else{
        alert("Odd")
    }
}


let pNz=()=>{
    let num=prompt("Enter a number")
    if(num>0){
        alert("positive")
    }else if(num===0){
        alert("Zero")
    }else{
        alert("Negative")
    }
}
// console.log(pNz())



let voteE=()=>{
    let age=prompt("Enter a number")
    if(age>=18){
        alert("iligible for voting")
    }else{
        alert("not iligible for voting")
    }
}
// console.log(voteE)

let largeOf2=()=>{
    let num1=prompt("Enter first number")
    let num2=prompt("Enter second number")
    if(num1>num2){
        alert("largestnum : "+num1)
    }else{
        alert("largestnum : " +num2)
    }
}
// console.log(largeOf2())


let passOrfail=()=>{
    let marks=prompt("Enter your marks")
    if(marks>=40){
        alert("Pass")
    }else{
        alert("fail")
    }
}
// console.log(passOrfail)

let gradeSystem=()=>{
    let marks=prompt("enter your mmarks");
    if(marks>90){
        alert("Grade A")
    }else if(marks<90 && marks>=70){
        alert("Grade B")
    }else if(marks<69 && marks>=50){
        alert("Grade C")
    }else if(marks<=50){
        alert("Grade Fail")
    }
}
// console.log(gradeSystem())

let largOf3=()=>{
    let a=prompt("Enter number1")
    let b=prompt("Enter number2")
    let c=prompt("Enter number3")
    if(a>b && b>c){
        alert("Largest : "+a)
    }else if(b>c && c>a){
        alert("Largest : "+b)
    }else
        alert("Largest : "+c)
}
// console.log(largOf3())

let leapYear=()=>{
    let year=prompt("Enter year number")
    if(year%4 !== year%100 || year%400 === 0)
        alert("Leap year")
    else
        alert("not a leap year")
}
// console.log(leapYear())

let guessNumber=()=>{
    let num=parseInt(prompt("guess number"));
    let chance=1
    let number=5;
    while(chance<=2 && num !== number){
        num=parseInt(prompt("wrong number plz try again"))
        chance++;
    }

        if(num === number){
            alert("you win")
        }else 
            alert("fail")
          
}
// console.log(guessNumber())

let reverse=()=>{
    let num1=parseInt(prompt("Enter number"))
    let num2=parseInt(prompt("Enter number"))
    let num3=parseInt(prompt("Enter number"))
    let num4=parseInt(prompt("Enter number"))
    let num5=parseInt(prompt("Enter number"))
    let arr=[num1,num2,num3,num4,num5]
    let rest=[]
    console.log(arr)
    for(let i=arr.length-1;i>=0;i--){
       rest.push(arr[i])
       }
      return rest;
}
// console.log(reverse())

let isPrime=()=>{
    let num=parseInt(prompt("Enter your choice"))

    for(let i=2;i<num;i++)
        if(num%i===0){
            alert("isprime")
        }else
            alert("not prime")
}
// console.log(isPrime())

let evenSum=()=>{
    let num=prompt("Enter your choise number")
    let sum=0;
    for(let i=0;i<=num;i++)
        if(i%2===0)
            sum+=i
        alert(+sum)
}

console.log(evenSum())

