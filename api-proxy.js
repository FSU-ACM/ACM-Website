require('dotenv').config()

const request = require('request')
const url = `https://graph.facebook.com/v2.11/ACMatFSU/events?access_token=${process.env.FACEBOOK_ACCESS_TOKEN}`

module.exports = (req, res) => {
    request(url, (err, resp, body) => {
        if (err) res.end(err)
        else res.end(body)
    })
}


