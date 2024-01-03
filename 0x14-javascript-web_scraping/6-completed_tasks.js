#!/usr/bin/node
/**
 * Computes the number of tasks completed by user id.
 */

const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const arr = {};
  const urlBody = JSON.parse(body);
  // console.log(urlBody);
  for (const task of urlBody) {
    const usrId = `${task.userId}`;
    if (task.completed) {
      if (usrId in arr) {
        arr[usrId]++;
      } else {
        arr[usrId] = 1;
      }
    }
  }
  console.log(arr);
});
