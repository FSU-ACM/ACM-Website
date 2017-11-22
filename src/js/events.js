// import http from 'http'

// http.get('http://proxy.localhost:8081', (resp) => {

//     let data = ''

//     // A chunk of data has been recieved.
//     resp.on('data', (chunk) => {
//         data += chunk
//     })

//     // The whole response has been received. Print out the result.
//     resp.on('end', () => {
//         document.getElementById('events').innerHTML = data
//     })

// }).on('error', (err) => {
//     console.log(err)
// })

$.get('https://proxy.acmatfsu.org', function(data) {
    console.log(data)
    $('#events').html(data)
})