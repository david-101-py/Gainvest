import sqlite3
from core.files_init import DATA_FILE

def _create_sql_tables():
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        #Table for the values of each account
        cursor.execute(f''' CREATE TABLE IF NOT EXISTS values_db (
                    account_id INTEGER PRIMARY KEY,
                    value FLOAT NOT NULL,
                    date DATE NOT NULL
        )''')
        #Table for the metadata of each account
        cursor.execute('''CREATE TABLE IF NOT EXISTS accounts_metadata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    group_id INTEGER DEFAULT NULL CHECK (group_id > 0),
                    birth_date DATE NOT NULL,
                    total_ignore BOOLEAN DEFAULT 0
        )''')
        #Table for the metadata of the groups and their parents
        cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    group_name TEXT NOT NULL UNIQUE,
                    parent_group INTEGER DEFAULT NULL CHECK (parent_group > 0),
                    birth_date DATE NOT NULL
        )''')

    conn.close()
