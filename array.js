let sum=()=>{
   let arr=[2,4,6,8,10];

   let sum=0;
   for(let i=0;i<=arr.length-1;i++){
     sum=sum+arr[i];
     
      }
      return sum;
}
console.log(sum());


let larg = () => {
  let arr = [7, 8, 6, 9, 2, 10];
  let max = arr[0];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i]; 
    }
  }
  return max;
};
console.log(larg())

let countEvenOdd=()=>{
    let arr=[1,2,3,4,5,6,7,8,9]

    let even=0;
    let odd=0;

    for(let i=0;i<arr.length;i++){
        if(i%2===0){
            even++
        }else{
            odd++
        }
    }
    return{
        even,odd
    }
}
console.log(countEvenOdd())

let reverse=()=>{
    let str=[1,2,3,4,5,6,7,8,9];
    let reverse=[];
    for(let i=str.length-1;i>=0;i--)
        reverse += str[i];
    return reverse;
}
console.log(reverse())

let find=()=>{
let numbers = [3, 5, 7, 9, 11];
let target = 9;

if (numbers.includes(target)) {
  console.log("yes,9 is in");
} else {
  console.log("no,9 is in");
}
}

console.log(find())

let concat=()=>{
  let a=[1,2,5,7]
  let b=[9,8,4]

  let result=[...a,...b];
  return result
}
console.log(concat())