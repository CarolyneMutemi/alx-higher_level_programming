#!/usr/bin/node

const dict1 = require('./101-data.js').dict;
const dict2 = {};
const dict1Keys = Object.keys(dict1);

for (const elem in dict1Keys) {
  const k = dict1[dict1Keys[elem]].toString();
  if (!dict2[k]) {
    dict2[k] = [dict1Keys[elem]];
  } else {
    dict2[k].push(dict1Keys[elem]);
  }
}

console.log(dict2);
