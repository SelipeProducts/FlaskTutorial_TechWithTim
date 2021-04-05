// function deleteNote(noteId){
//   fetch("/delete-note", {
//     method: "POST",
//     credentials: 'same-origin',
//     body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     console.log(_res)
//     window.location.href = "/";
//   });
// }

//Working with get mothod
// function deleteNote(noteId){
//   fetch("/delete-note").then(res => res.json()).then(data => console.log(data));
// }
function deleteNote(noteId){
  fetch('/delete-note', {
    method: 'POST',
    body: JSON.stringify({noteId: noteId})
  }).then((_res) => {
    window.location.href = "/"
  });
}
//LAST TEST
// function deleteNote(noteId){
//   fetch("/delete-note/", {    
//     // Adding method type
//     method: "POST",
//     // Adding body or contents to send
//     body: JSON.stringify({ noteId: noteId }),
//     // Adding headers to the request
//     headers: {
//         "Content-Type": "application/json; charset=UTF-8"
//     }
//   }).then(res => res.json()).then(data => console.log(data));
// }
// function axiosmethod(noteId){
//     axios({
//     method: 'post',
//     url: '/delete-note/',
//     data: {noteId: noteId}
//   }).then((response) => {
//   console.log(response);
//   }, (error) => {
//     console.log(error);
//   });
    // var axios = require('axios');

  // var config = {
  //   method: 'POST',
  //   url: '/delete-note/',
  //   data: {noteId: noteId}
  // };
  
  // axios(config)
  // .then(function (response) {
  //   console.log(JSON.stringify(response.data));
  // })
  // .catch(function (error) {
  //   console.log(error);
  // });


// function loadXMLDoc(num) {
//   console.log("HEllo "+ num)

//   var xhttp = new XMLHttpRequest();

  // xhttp.onreadystatechange = function() {
  //   if (this.readyState == 4 && this.status == 200) {
  //     console.log("Working")
  //   }
  //   else{
  //     console.log("ERROR")
  //     console.log("Status: ", this.status)
  //     console.log("Ready State: ", this.readyState)
  //   }
  // };
//   xhttp.open("POST", "/delete-note/", true);
//   xhttp.onclick() = () => {
//     console.log(xhr.response)
//   };


//   xhttp.send();
// }

// function deleteNote(noteId){
//   console.log("hello is there anybody in there")
//   fetch("https://raw.githubusercontent.com/terrenjpeterson/caloriecounter/master/src/data/foods.json").then(res =>
//     res.json()).then(data => console.log('DATA: ' + data);
// }

// function deleteNote(noteId) {
//   fetch("https://flasktutorialtechwithtim.cesarlopez200.repl.com/delete-note", {
//     method: "POST",
//     body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     window.location.href = "/";
//   }).catch(err => console.error('Caught error: ', err));

// }



//.catch((error) => {
//   console.log(error)
// })
//Get note id that we past. send post request to to /delete-note endpoint. After getting a response from endpoint, reload the window with get request
