#!/usr/bin/node
/**
 * Gets the contents of a webpage and stores it in a file.
 */

const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(file, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
