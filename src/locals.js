// locals.js
var locals = {};

locals.css = "./public/css";
locals.img = "./public/img";
locals.js  = "./public/js";

locals.events = require("./events.json").events;
locals.officers = require("./views/officers/officers.json").officers;
locals.partners = require("./views/sponsors/partners.json").partners;
locals.sponsors = require("./views/sponsors/sponsors.json").sponsors;

module.exports = locals;
