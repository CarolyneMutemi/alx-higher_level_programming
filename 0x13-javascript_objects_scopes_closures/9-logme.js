#!/usr/bin/node

let track = 0;
exports.logMe = function (item) {
  /**
     * Prints the number of arguments already printed and the new argument value.
     */
  console.log(`${track}: ${item}`);
  track += 1;
};
