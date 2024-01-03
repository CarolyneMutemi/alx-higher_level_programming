#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie.
 */

const request = require('request');
const process = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
