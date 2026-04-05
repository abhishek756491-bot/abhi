
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