#!/usr/bin/node
/**
 * Imports an array and computes a new array.
 */

const arr = require('./100-data.js').list;
let i = 0;
const arr2 = arr.map((x) => x * i++);
console.log(arr);
console.log(arr2);
