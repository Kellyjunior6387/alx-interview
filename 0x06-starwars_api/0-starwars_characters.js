#!/usr/bin/node
'use strict';
const request = require('request');
const filmUrl = 'https://swapi-api.alx-tools.com/api';
const filmId = process.argv[2];
if (isNaN(filmId)) {
  throw new Error('Film ID must be an integer');
}

request(`${filmUrl}/films/${filmId}/`, (error, _, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  const charactersName = characters.map(
    url => new Promise((resolve, reject) => {
      request(url, (error, __, charactersBody) => {
        if (error) {
          reject(error);
        }
        resolve(JSON.parse(charactersBody).name);
      });
    }));

  Promise.all(charactersName)
    .then(names => console.log(names.join('\n')))
    .catch(allErr => console.log(allErr));
});
