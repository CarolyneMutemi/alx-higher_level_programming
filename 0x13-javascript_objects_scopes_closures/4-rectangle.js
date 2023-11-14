#!/usr/bin/node
/*
 * Creates a class Rectangle that defines a rectangle.
 */

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    /*
        Prints the rectangle using the character X.
         */
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  rotate () {
    /*
        Exchanges the width and the height of the rectangle.
         */
    const h = this.height;
    this.height = this.width;
    this.width = h;
  }

  double () {
    /*
        Multiples the width and the height of the rectangle by 2.
         */
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
