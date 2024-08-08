const fs = require('fs');

// Read the JSON file
const data = JSON.parse(fs.readFileSync('/home/nyams/alx-interview/0x06-starwars_api/sample.json'));

// Extract the names of the characters
const names = data.results.map(character => character.name);

// Print the names
names.forEach(name => console.log(name));
