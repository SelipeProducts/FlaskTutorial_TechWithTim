// function deleteNote(noteId){

//   fetch("/delete-note", {
//     method: "POST",
//     body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     window.location.href = "/logout";
//   });
// }

function deleteNote(noteId) {
  fetch("https://flasktutorialtechwithtim.cesarlopez200.repl.com/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  }).catch(err => console.error('Caught error: ', err));

}



//.catch((error) => {
//   console.log(error)
// })
//Get note id that we past. send post request to to /delete-note endpoint. After getting a response from endpoint, reload the window with get request
