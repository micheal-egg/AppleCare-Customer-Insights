

# Reads SQL schema from sql/schema.sql to create tables
# This will read the csv files content from the sample survey I made

import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = "voc.db"
SCHEMA_PATH = Path("sql/schema.sql")
CSV_PATH = Path("data/raw/sample_surveys.csv")

#For Table creation 
def init_schema(db_path: str = DB_PATH, schema_path: Path = SCHEMA_PATH) -> None: #Reads SQL Schema creating tables in voc.dv
    # Function perfoms an action but does not return anything
    # Create tables if they don't exist using the schema.sql file.
    sql = schema_path.read_text(encoding="utf-8")
    con = sqlite3.connect(db_path)
    con.executescript(sql)   # executes multiple SQL statements
    con.commit()
    con.close()

def load_surveys(csv_path: Path = CSV_PATH, db_path: str = DB_PATH) -> int:
    # Load CSV into 'surveys' table. Returns number of rows loaded.
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at {csv_path}") #Maual error message

    df = pd.read_csv(csv_path) #This will load the CSV into a panda dataframe

    # Apply transformations (PII redaction, normalization)
    from etl.transform import transform
    df = transform(df) 

    con = sqlite3.connect(db_path)
    # Replace during development so it can re-run easily
    df.to_sql("surveys", con, if_exists="replace", index=False)
    con.close()
    return len(df)

def main():
    init_schema()
    n = load_surveys()
    print(f"✅ Database ready at '{DB_PATH}'. Loaded {n} survey rows into 'surveys'.")

if __name__ == "__main__":
    main()