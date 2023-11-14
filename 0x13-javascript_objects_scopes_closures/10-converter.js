#!/usr/bin/node

exports.converter = function (base) {
  /**
     * Converts a number from base 10 to another base passed as argument.
     */
  function convert (num) {
    return num.toString(base);
  }
  return convert;
};
