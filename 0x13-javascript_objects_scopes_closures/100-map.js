#!/usr/bin/node
/**
 * Imports an array and computes a new array.
 */

const arr1 = require('./100-data.js').list;

console.log(arr1);
console.log(arr1.map((x) => x * arr1.indexOf(x)));
