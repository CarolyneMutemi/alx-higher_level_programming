#!/usr/bin/node
/**
 * Reads and prints the content of a file.
 */

const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
