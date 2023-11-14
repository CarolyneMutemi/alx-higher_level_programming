#!/usr/bin/node
/**
 * Imports an array and computes a new array.
 */

const arr1 = require('./100-data.js').list;
let arr2 = [];
if (arr1.length > 0) {
  arr2 = arr1.map((x) => x * arr1.indexOf(x));
}
console.log(arr1);
console.log(arr2);
