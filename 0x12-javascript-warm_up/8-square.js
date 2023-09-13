#!/usr/bin/node
let a;
let b;
let r = '';
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size))
{
  console.log('Missing size');
}
else
{
  for (a = 0; a < size; a++)
  {
    let r  = '';
    for (b = 0; b < size; b++) r += 'X';
    console.log(r);
  }
}
