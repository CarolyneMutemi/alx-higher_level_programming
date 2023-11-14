#!/usr/bin/node

/**
 * Defines a square and inherits from Square of 5-square.js
 */

const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    /**
         * Prints the rectangle using the character c.
         * If c is undefined, use the character X.
         */

    if (!c) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
}

module.exports = Square;
