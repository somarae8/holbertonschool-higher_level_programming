#!/usr/bin/node
// Square class that inhererit from Rectangle::
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
