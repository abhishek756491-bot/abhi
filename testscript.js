let evenNodd = () => {
    let arr = [3, 0, 2, 12, 15, 19];
    let countEven = 0;
    let countOdd = 0;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 === 0) {
            countEven++;
        } else {
            countOdd++;
        }
    }

    let resultArr = [countEven, countOdd];
    return resultArr;
}

console.log(evenNodd());


function toggle() {
  let x = document.getElementById("text");
  
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
console.log(toggle())



array=[{
    name:"arhan",
    city:"muzaffar",
    age:25,
    college:"rmls"
},{
    name:"murshid",
    city:"samastipu",
    age:28,
    college:"rmls"
},{
    name:"murshid",
    city:"bihar",
    age:29,
    college:"rmls"
}]
let show=document.querySelector(".show")

array.map((i)=>{
    show.innerHTML += `

<div >
  <h1> ${i.name}</h1>
  <h3> ${i.city}</h3>
  <h3> ${i.age}</h3>
  <h3> ${i.college}</h3>
</div>
 `

})


let formValidate=()=>{
     let name =document.querySelector("#name").value.trim();
    let num =document.querySelector("#num").value.trim();

    let ErrName =document.querySelector("#errname");
    let ErrNum =document.querySelector("#errnum");


     if(name == ""){
        ErrName.innerHTML="please Enter your Name"
        return false;
    } 
      else
        ErrName.innerHTML="";

    if(num == ""){
        ErrNum.innerHTML="please Enter your Number";
        return false;
    }
   
    if(num.length !== 10){
        ErrNum.innerHTML="please Enter 10 digit number";
        return false;
    }
}
