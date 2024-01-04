#!/usr/bin/node
/**
 * Prints the number of movies where the character “Wedge Antilles” is present.
 */

const process = require('process');
const request = require('request');

const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const bod = JSON.parse(body);
  const movies = bod.results;
  for (let index = 0; index < movies.length; index++) {
    const movie = movies[index];
    for (const character of movie.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
