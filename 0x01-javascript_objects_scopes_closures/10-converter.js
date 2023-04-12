#!/usr/bin/node
exports.converter = function (base) {
  return function (check) {
    return check.toString(base);
  };
};
