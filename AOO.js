let fruits = ["apple", "banana","orange","kiwi"]
console.log(fruits[0])

let info = [{
    name:"Ravi",
    age:45,
    ghar:"Bhopal"
},{
    name:"Ravi",
    age:45,
    ghar:"Bhopal"
},{
    name:"Ravi",
    age:45,
    ghar:"Bhopal"
}]

// console.log(info[1])

let num=[4,7,5,6,9,5,4,7]

let newarray= num.map((e)=>{
    return   e%2==0;
})
// console.log(newarray);

let newfilter =num.filter((e)=>{
    return e%2==0;
})
console.log(newfilter)


 