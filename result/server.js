const express = require("express");
const { Pool } = require("pg");

const app = express();
const pool = new Pool({
  user: "postgres",
  host: "db",
  database: "postgres",
  password: "postgres",
  port: 5432,
});

app.get("/", async (req, res) => {
  const { rows } = await pool.query("SELECT vote, COUNT(*) as count FROM votes GROUP BY vote;");
  let output = "<h2>Results</h2><ul>";
  rows.forEach(r => {
    output += `<li>${r.vote}: ${r.count}</li>`;
  });
  output += "</ul>";
  res.send(output);
});

app.listen(80, () => console.log("Result app running on port 80"));

