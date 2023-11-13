#!/usr/bin/node

/*
 * Searches the second biggest integer in the list of arguments.
 */

const input = process.argv;
let big = input[0];
let second = 0;
let i = 2;

while (i < input.length && input.length !== 3) {
  if (input[i] > big) {
    second = big;
    big = input[i];
  }
  i++;
}

console.log(second);
