#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie.
 */

const request = require('request');
const process = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const list = [];
let name = null;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (let idx = 0; idx < characters.length; idx++) {
    request(characters[idx], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      name = JSON.parse(body).name;
      console.log(name);
      list[idx] = name;
      // console.log(JSON.parse(body).name);
    });
  }
});
console.log(list);
