import sqlite3
import datetime
from core.files_init import DATA_FILE

def get_id(name, is_account=True):
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        if is_account:
            cursor.execute("SELECT id FROM accounts_metadata WHERE name = ?", (name,))
        else:
            cursor.execute("SELECT group_id FROM groups WHERE group_name = ?", (name,))
        result = cursor.fetchone
        if result:
            id = result[0]
        else:
            id = None
        conn.close()
    return id

def delete_account(name):
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        account_id = cursor.execute("SELECT id FROM accounts_metadata WHERE name = ?", (name,))
        cursor.execute(f"DELETE FROM values_db WHERE account_id = ?", (account_id,))
    conn.close()

def clear_last_values(account_name, last_values):
    account_id = get_id(account_name)
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(''' 
            DELETE FROM values_db 
            WHERE rowid IN (
                SELECT rowid FROM values_db 
                WHERE account_id = ? 
                ORDER BY date DESC 
                LIMIT ?)
        ''', (account_id, last_values))
    conn.close()

def give_values_to_account(account_id, value):
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO values_db (account_id, value, date) 
        VALUES (?, ?, ?)''' , (account_id, value, datetime.now().strftime("%Y-%m-%d %H:%M:%S") ))
    conn.close()

def create_account(account, group=None):
    group_id = get_id(group, is_account=False) if group else None
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        if group != None:
            cursor.execute('''
            INSERT INTO accounts_metadata (name, group_id, birth_date) 
            VALUES (?, ?, ?, ?)''', (account, group_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S") ))
        else:
            cursor.execute('''
            INSERT INTO accounts_metadata (name, birth_date) 
            VALUES (?, ?, ?)''', (account, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))    
    conn.close()
    return account

def change_account_group(name, parent_group) -> None:
    id = get_id(name)
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE series_metadata
            SET group_id = (SELECT group_id FROM groups WHERE group_name = ?)
            WHERE account_id = ?;
 ''', (parent_group, id))
    conn.close()

def change_parent_group(group_name, parent_group) -> None:
    id = get_id(group_name, is_account=False)
    with sqlite3.connect(DATA_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE groups
        SET parent_group = (SELECT group_id FROM groups WHERE group_name = ?)
        WHERE group_id = ?;
''', (parent_group, id))
    conn.close()



