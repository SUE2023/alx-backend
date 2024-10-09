#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Callback function to print the response
const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, (err, reply) => {
    if (err) {
      console.log('Error setting value:', err);
    } else {
      console.log(`SET response: ${reply}`);
    }
  });
};

// Fetch and display the value of a key
const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (err, reply) => {
    if (err) {
      console.log('Error getting value:', err);
    } else {
      console.log(`GET ${schoolName}: ${reply}`);
    }
  });
};

// Test the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

