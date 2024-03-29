#!/usr/bin/node
const request = require('request');
const users = {};
request(process.argv[2], 'utf8', function (err, response, body) {
  if (err) throw err;
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      if (users[task.userId]) {
        users[task.userId]++;
      } else {
        users[task.userId] = 1;
      }
    }
  }
  console.log(users);
});
