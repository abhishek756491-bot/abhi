//      function Abhi(){
//       alert ("hello twice")
//       let Text = document.getElementById('text1')
// //     let Text = document.getElementByClassName('text1')
// //    let Text = document.querySelector('#text1')
//   Text.innerHTML = "this text is from js"
//  }

function Hide(){
    let Text =document.querySelector('#text1')
    Text.style.visibility="hidden"
}
function Show(){
    let Text =document.querySelector('#text1')
    Text.style.visibility="visible"
}

let c=0;
function Inc(){
  let text = document.querySelector('#text')
  c++
  text.innerHTML=c
}
function Dec(){
  let text = document.querySelector('#text')
  
  if(c<=0){
    return
  }
  c--
  text.innerHTML=c 
}
// //array , prompt , loop ,bom,dom,alert

function photo(){
    let seen = document.querySelector("#boxpic")
    seen.style.backgroundImage ="url('date.png')";
    seen.style.backgroundSize="cover"
}

// let h2 = document.querySelector("h2");
// console.dir(h2.innerText);
// h2.innerText = h2.innerText + " and I am from Bihar";

//let divs = document.querySelectorAll(".box")
// // console.log(divs);
// divs[0].innerText = "this is a unique1";
// divs[1].innerText = "this is a unique1";
// divs[2].innerText = "this is a unique2";

//in loop 
// let idx = 1;
// for (div of divs){
//   div.innerText= `new unique value ${idx}`
//   idx++;
// }

// let newBtn = document.createElement("button");
// newBtn.innerText = "Click me!";

// newBtn.style.color = "white";
// newBtn.style.backgroundColor = "red";

// document.querySelector("body").prepend(newBtn);
 
function colorred(){
let pic = document.querySelector(".box")
pic.style.backgroundColor = "red";
}

function colorgreen(){
let pic = document.querySelector(".box")
pic.style.backgroundColor = "green";
}

function colorblue(){
let pic = document.querySelector(".box")
pic.style.backgroundColor = "blue";
}
 
//counter program

let count=0;

function IncBtn(){
    let Inc = document.querySelector("#num")
    count++;
    Inc.innerHTML = count;
}

function ResetBtn(){
    let Reset = document.querySelector("#num")
    count = 0;
    Reset.innerHTML = count;
}

function DecBtn(){
    let Dec = document.querySelector("#num")
    count--;
    Dec.innerHTML = count;
}

// JavaScript function to update the h1 tag
        function updateH1() {
            // Get the input element using its ID
            const inputElement = document.getElementById('textInput').value;
            convertH1.innerHTML=inputElement
        }


        function changeBoxColor() {
            // Get the value from the input field
            let colorValue = document.getElementById("colorInput").value;
            
            // Get the reference to the target box element
            let box = document.getElementById("targetBox");
            
            // Apply the input value as the background color
            // The browser will only apply valid CSS color values
            box.style.backgroundColor = colorValue;
        }



// //arow function
//         let App=(a)=>a*a
//         console.log(App(4));
    
