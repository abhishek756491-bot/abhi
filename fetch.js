//js is syncronus language

// let data;
// let getData=async ()=>{
//       let Api='https://jsonplaceholder.typicode.com/posts'

//       let res=await fetch(Api)

//       let data=await res.json()

//     console.log(data)

 
// let dat=document.querySelector(".bod")

// data.map((e)=>{
//     dat.innerHTML+= `
   
    
//      <div>
//         <p>${e.userId}</p>
//         <p>${e.id}</p>
//         <p>${e.title}</p>
//         <p>${e.body}</p>
//      </ div>

//      `
// })
// }
// getData()


let fetchdata=async ()=>{
    let Api='https://jsonplaceholder.typicode.com/posts'

    let response= await fetch(Api,{method:"Get"})
    let mydata= await response.json()

    console.log(mydata)

    let show=document.querySelector("#show")
    mydata.map((e)=>{
        show.innerHTML +=
        `
        <tr>
          <td> ${e.id}</td>
          <td> ${e.title}</td>
          <td> ${e.body}</td>
        </tr>
        `
    })

}
