#!/usr/bin/node
function add (a, b) {
  return a + b;
}
a = Number(process.argv[2]);
b = Number(process.argv[3]);
console.log(add(a, b));
