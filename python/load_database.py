import pandas as pd
import sqlite3

csv_file = "data/blinkit_cleaned.csv"
database_file = "database/blinkit.db"

df = pd.read_csv(csv_file)

conn = sqlite3.connect(database_file)

df.to_sql(
    "blinkit",
    conn,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into SQLite!")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM blinkit")

count = cursor.fetchone()[0]

print("Total records:", count)

conn.close()