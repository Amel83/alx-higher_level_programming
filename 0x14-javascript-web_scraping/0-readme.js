#!/usr/bin/node

const fss = require('fs');
const file = process.argv[2];

fss.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
