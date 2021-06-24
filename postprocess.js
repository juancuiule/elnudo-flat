const fs = require('fs')


console.log("Algo")

fs.readFile('./data.json', (err, data) => {
    console.log(data)
})