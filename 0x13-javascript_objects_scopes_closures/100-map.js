#!/usr/bin/node
/**
 * Imports an array and computes a new array.
 */

const arr1 = require('./100-data.js').list;
let i = 0;
const arr2 = arr1.map((x) => x * i++);
console.log(arr1);
console.log(arr2);
