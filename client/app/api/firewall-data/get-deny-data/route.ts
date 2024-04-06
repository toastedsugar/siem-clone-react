const sqlite3 = require("sqlite3").verbose();
import { open, Database } from "sqlite";


const path = require('path')


//export const dynamic = "force-dynamic"; // defaults to auto

let db:any = null

export async function GET(request:Request, response:Response) {
  const dbPath = path.join(__dirname, "../../../../../data/data.db")
  console.log(dbPath)
  // Check if the database instance has been initialized
  if (!db) {
    // If the database instance is not initialized, open the database connection
    db = await open({
      filename: dbPath, // Specify the database file path
      driver: sqlite3.Database, // Specify the database driver (sqlite3 in this case)
    });
  }

  // Perform a database query to retrieve all items from the "items" table
  const items = await db.all("SELECT * FROM firewall_data");

  // Return the items as a JSON response with status 200
  return new Response(JSON.stringify(items), {
    headers: { "Content-Type": "application/json" },
    status: 200,
  });
}










/*
export async function GET(request: Request) {
  const db = new sqlite3.Database(
    "@/data/data.db",
    sqlite3.OPEN_READONLY,
    (err: any) => {
      if (err) return console.error(err.message);
    }
  );

  const sql = 'SELECT action FROM firewall_data WHERE action = ?'

  await db.each(sql, ['deny'], (err: any, row:any) => {
    console.log(row, err)
  })

  console.log("!")
  return Response.json({firewall: 'firewall'})
}
*/