
let ram=()=>{
  let abhi =document.querySelector("#abh").value.trim();

let details={
    name:abhi,
    roll:45,
    College:"radha"
}
console.log(details.name)
}


// details.roll=49 //update
// details.mynumber=97849851698 //insert
// delete details.name
// console.log(details) //access

//destructuring the object
// let arr = [45,78,86,48,68,25]
// let   [a,b,c, ...rest]=arr;

// let {d,e,f}={d:56,e:89,f:91}

// let student={name:"abhishek kumar",age:24,cl:"b.tech"}
// let {name,age,cl}=student;

//spead Operater
let arr1 = [7,8,9]
let obj1 ={...arr1}
let obj2 ={age:95,name:"abhishek",gar:"muzaffarpur"}
let obj3 ={grade:"A",number:98}
let combined={...obj2,obj1,...obj3}
console.log(combined)