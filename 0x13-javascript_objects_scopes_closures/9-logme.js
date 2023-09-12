#!/usr/bin/node
let norg = 0;

exports.logMe = function (item) {
  console.log(norg + ': ' + item);
  norg++;
};
