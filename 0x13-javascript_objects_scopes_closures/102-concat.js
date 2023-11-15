#!/usr/bin/node

/**
 * Concats 2 files.
 */

const fs = require('fs');

fs.readFile(process.argv[2], function (err, data) {
  if (err) {
    return console.error(err);
  }
  const file1 = data.toString();

  fs.readFile(process.argv[3], function (err, data) {
    if (err) {
      return console.error(err);
    }
    const file2 = data.toString();

    fs.writeFile(process.argv[4], `${file1}${file2}`, function (err) {
      if (err) {
        return console.error(err);
      }
    });
  });
});
