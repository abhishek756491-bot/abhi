let sum=()=>{
   let arr=[2,6,8,10]
   let print=document.querySelector("#print");
   let sum=0
   
   for(let i=0;i<=arr.length-1;i++){
     sum=sum+arr[i]
     print.innerHTML=sum;
   }
}
let larg=()=>{
    let arr=[7,8,6,9,2,10]
    for(let i=0;i<=arr.length-1;i++){
        if(arr[0]>arr[1])
            console.log(arr[0])
    }
}
console.log(larg())