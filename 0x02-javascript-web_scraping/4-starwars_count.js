#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let mc = 0;
request(url, (err, response, body) => {
  if (err) throw err;
  const data = JSON.parse(body).results;
  for (const title in data) {
    const chars = data[title].characters;
    for (const person in chars) {
      if (chars[person].includes('/18')) {
        mc++;
      }
    }
  }
  console.log(mc);
});
