#!/usr/bin/node
/**
 * A script that display the status code of a GET request.
 */

const request = require('request');
const process = require('process');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: %s', response.statusCode);
});
