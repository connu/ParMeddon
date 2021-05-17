
// function e()
// {
//     fetch('/hello', {

//         // Declare what type of data we're sending
//         headers: {
//           'Content-Type': 'application/json'
//         },
    
//         // Specify the method
//         method: 'POST',
    
//         // A JSON payload
//         body: JSON.stringify({
//             "greeting": "Hello from the browser!"
//         })
//     }).then(function (response) { // At this point, Flask has printed our JSON
//         return response.text();
//     }).then(function (text) {
    
//         console.log('POST response: ');
    
//         // Should be 'OK' if everything was successful
//         console.log(text);
//     });

// }

// fetch('/hello', {

//     // Declare what type of data we're sending
//     headers: {
//       'Content-Type': 'application/json'
//     },

//     // Specify the method
//     method: 'POST',

//     // A JSON payload
//     body: JSON.stringify({
//         "greeting": "Hello from the browser!"
//     })
// }).then(function (response) { // At this point, Flask has printed our JSON
//     return response.text();
// }).then(function (text) {

//     console.log('POST response: ');

//     // Should be 'OK' if everything was successful
//     console.log(text);
// });
var script = document.createElement("SCRIPT");
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName("head")[0].appendChild(script);


function e()
{
    $.post( "/hello", {
        'javascript_data': 'ello'
    });
}