const { Pool } = require('pg');
const http = require('http');

const pool = new Pool({
  user: 'root',
  host: '0.0.0.0',
  database: 'postgres',
  password: 'root',
  port: '5432',
});

const server = http.createServer((req, res) => {
  // Set the response headers to allow cross-origin requests and indicate that the response will be JSON
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Content-Type', 'application/json');

  // Execute a query to retrieve data from the database
  pool.query('SELECT * FROM ad', (err, result) => {
    if (err) {
      console.error(err);
      res.statusCode = 500;
      res.end(JSON.stringify({ error: 'Internal Server Error' }));
    } else {
      // Return the query result as JSON
      res.statusCode = 200;
      res.end(JSON.stringify(result.rows));
    }
  });
});

const port = 3000;
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
