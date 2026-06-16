import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

df = pd.read_sql_query(
    "SELECT * FROM sales LIMIT 10",
    conn
)

print(df)

conn.close()