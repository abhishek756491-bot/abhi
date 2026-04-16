
function btn(){
    let writearea=document.querySelector("#write").value;
   let print=document.querySelector("#print");

    let area=writearea.toUpperCase();
    print.innerText=area;
}

function btntolower(){
    let writearea=document.querySelector("#write").value;
   let print=document.querySelector("#print");

    let area=writearea.toLowerCase();
    print.innerText=area;
}

function btnlength(){
    let writearea=document.querySelector("#write").value;
   let print=document.querySelector("#print");

    let area=writearea.length;
    print.innerText=area;
}

function btnreverse(){
    let writearea=document.querySelector("#write").value;
   let print=document.querySelector("#print");

    let reversedstr="";
   for(let i=writearea.length-1;i>=0;i--){
       reversedstr+=writearea[i]
    
    print.innerHTML=reversedstr;
    }
}

function btncountvowel(){
    let writearea=document.querySelector("#write").value;
   let print=document.querySelector("#print");

   let count=0;
   for(let i=0;i<writearea.length;i++)
   {
    let char=writearea[i];
  
    if(char === 'a' || char === 'e'  || char === 'i'  || char === 'o'  || char === 'u' 
         || char === 'A'  || char === 'E'  || char === 'I'  || char === 'O'  || char === 'U' )
      
       count++;
     }
    print.innerHTML=count;
    }

    function  pelindrome(){
     let str=prompt("Enter")

     let reversestr="";

     for(let i=str.length-1;i>=0;i--)
     {
        reversestr +=str[i];
    }
        if(str.toLowerCase() === reversestr.toLowerCase())
            alert(str+" it is pelindrome")
        else
            alert(str+" it is not pelindrome")
     
    }
    // console.log(pelindrome())

    let btnremove=()=>{
        let writearea=document.querySelector("#write").value;
        let print=document.querySelector("#print");

        let str="";
        for(let i=0;i<writearea.length;i++)
        {
            if(writearea[i] !== " "){
            str+=writearea[i];
            }
        }
        print.innerHTML=str;
    }

    function excespace(){
    let writearea=document.querySelector("#write").value;
   let print=document.querySelector("#print");

   let count=0;
   for(let i=0;i<writearea.length;i++)
   {
    let char=writearea[i];
  
    if(char !== " ")
       count++;
     }
    print.innerHTML=count;
    }

    let btnfirst=()=>{
         let writearea=document.querySelector("#write").value;
         let print=document.querySelector("#print");
      
             let result=writearea.charAt(0).toUpperCase()+writearea.slice(1);
             print.innerHTML=result;
            
    }

    
     let countword=()=>{
         let writearea=document.querySelector("#write").value.trim();
         let print=document.querySelector("#print");
      
      let result=writearea.split(" ").length;
       print.innerHTML=result;
      
    }
    let EvenNodd=()=>{
    let n=prompt("Enter our number")
    if(n%2===0)
        alert("Even")
    else
        alert("Odd")
}
// console.log(EvenNodd())

let count=()=>{
    let n=prompt("Enter your choice");
    let l=n.length;
    alert(+l)
}
// console.log(count())

let uppercase=()=>{
    let n=prompt("Enter your choice")
    let l=n.toUpperCase();
    alert(l)
}
// console.log(uppercase())

let sum=()=>{
    let arr =[]
    let sum=0
    for(let i=1;i<=5;i++){
        let input=Number(prompt("Enter number "+(i)))
        arr.push(Number(input));
    }
    for(let i=0;i<arr.length;i++)
     sum=sum+arr[i]
      alert(+sum)
    
}
// console.log(sum())


let reverse=()=>{
    let input=document.querySelector(".input").value;
    let print=document.querySelector(".print");

    let reversedstr="";
    for(let i=input.length-1;i>=0;i--){
        reversedstr+=input[i]
    
    print.innerHTML=reversedstr;
    }
//   console.log(reverse())

}
let even=()=>{
    
    let arr =[]
    let count=1
     for(let i=1;i<=5;i++){
        let input=prompt("Enter number "+(i))
        arr.push(Number(input));
      }

     for(let i=0;i<arr.length;i++){
        if(arr[i] %2 === 0){
            count++;
        }
         console.log(+count)
    }
}
// console.log(even())

