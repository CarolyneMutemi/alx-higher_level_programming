#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  const newList = [];
  let index = 0;
  while (len >= 0) {
    newList[index] = list[len];
    index++;
    len--;
  }
  return newList;
};
