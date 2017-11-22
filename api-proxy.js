require('dotenv').config()

const request = require('request')
const pug = require('pug')
var hdate = require('human-date')

const url = `https://graph.facebook.com/v2.11/ACMatFSU/events?access_token=${process.env.FACEBOOK_ACCESS_TOKEN}`

module.exports = (req, res) => {
    request(url, (err, resp, body) => {
        if (err) res.end(err)
        else {
            let locals = {}
            let events = JSON.parse(body).data

            // Filter dates
            let cutoff = new Date(new Date().setFullYear(new Date().getFullYear() - 1))

            events = events.filter((item) => {
                return new Date(item.start_time) >= cutoff
            })

            // Make date friendly
            events.forEach(element => {
                element.start_time = hdate.prettyPrint(new Date(element.start_time))
            })

            let fn = pug.compileFile('src/views/_includes/events.pug')
            // res.end(fn(locals))
            // console.log(fn(locals))

            locals.events = events
            res.setHeader('Access-Control-Allow-Origin', '*')
            res.end(fn(locals))
        }
    })
}


