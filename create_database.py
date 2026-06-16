import pandas as pd
import sqlite3

df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

conn = sqlite3.connect("sales.db")

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.commit()
conn.close()

print("Database Created Successfully")