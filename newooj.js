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