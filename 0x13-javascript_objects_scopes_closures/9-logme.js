#!/usr/bin/node
let count = 0;
exports.logMe = function (k) { console.log(`${count++}: ${k}`); };
