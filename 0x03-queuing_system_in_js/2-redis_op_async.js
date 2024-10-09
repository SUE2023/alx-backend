#!/usr/bin/yarn dev
import { createClient } from 'redis';
import { promisify } from 'util';  // Import promisify

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

// Promisify the GET method
const getAsync = promisify(client.GET).bind(client);

// Promisify the SET method
const setAsync = promisify(client.SET).bind(client);

// Function to set a new school in Redis
const setNewSchool = async (schoolName, value) => {
  try {
    const reply = await setAsync(schoolName, value);
    console.log(`SET response: ${reply}`);
  } catch (err) {
    console.log('Error setting value:', err);
  }
};

// To get and display school value (using async/await)
const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await getAsync(schoolName);
    console.log(`GET ${schoolName}: ${reply}`);
  } catch (err) {
    console.log('Error getting value:', err);
  }
};

// Testing the functions using async/await
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();

