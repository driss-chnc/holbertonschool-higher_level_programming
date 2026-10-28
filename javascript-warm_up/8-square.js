#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  let line = '';

  while (i < size) {
    line += 'X';
    i++;
  }

  i = 0;

  while (i < size) {
    console.log(line);
    i++;
  }
}
