// let fruits = ["apple", "banana","orange","kiwi"]
// console.log(fruits[0])

// let info = [{
//     name:"Ravi",
//     age:45,
//     ghar:"Bhopal"
// },{
//     name:"Ravi",
//     age:45,
//     ghar:"Bhopal"
// },{
//     name:"Ravi",
//     age:45,
//     ghar:"Bhopal"
// }]

// // console.log(info[1])

// let num=[4,7,5,6,9,5,4,7]

// let newarray= num.map((e)=>{
//     return   e%2==0;
// })
// // console.log(newarray);

// let newfilter =num.filter((e)=>{
//     return e%2==0;
// })
// console.log(newfilter)



let infor = [{
    name:"Abhinav",
    roll:"45",
    corse:"full",
    branch:"cse",
    image:"thar rox.jpeg"

},{
    name:"Abhinash",
    roll:"50",
    corse:"Ds",
    branch:"cse sp",
    image:"defender.jpeg"
},{
    name:"Abhisir",
    roll:"46",
    corse:"DA",
    branch:"Mba",
    image:"fortuner.jpeg"
},{
    name:"Naman",
    roll:"49",
    corse:"finance minister",
    branch:"bba",
    image:"land cruiser.jpeg"
}]

let show = document.querySelector("#Show");
  
infor.map((i)=>{
 show.innerHTML += `

<div>
  <img src="${i.image}" width=100px height=100px>
  <h1> ${i.name}</h1>
  <h3> ${i.roll}</h3>
  <h3> ${i.corse}</h3>
  <h3> ${i.branch}</h3>
</div>
 `
 })