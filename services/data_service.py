from datetime import datetime
from core.db_core import execute

def get_id(name, is_account=True):
    if is_account:
        result = execute("SELECT id FROM accounts_metadata WHERE name = ?", (name,), fetch="one")
    else:
        result = execute("SELECT group_id FROM groups WHERE group_name = ?", (name,), fetch="one")
    id = None if result == None else result[0]
    return id

def delete_account(name):
    id = get_id(name)
    execute("DELETE FROM values_db WHERE account_id = ?", (id,), commit=True)
    execute("DELETE FROM accounts_metadata WHERE id = ?", (id,), commit=True)

def clear_last_values(name, last_values):
    id = get_id(name)
    execute(''' 
            DELETE FROM values_db 
            WHERE rowid IN (
                SELECT rowid FROM values_db 
                WHERE account_id = ?
                ORDER BY date DESC 
                LIMIT ?)
        ''', (id, last_values), commit=True)

def give_values_to_account(name, value):
    id = get_id(name)
    execute('''
        INSERT INTO values_db (account_id, value, date) 
        VALUES (?, ?, ?)''' , (id, value, datetime.now().strftime("%Y-%m-%d %H:%M:%S") ))

def create_account(account, group=None):
    if group != None:
        group_id = get_id(group, is_account=False)
        execute('''
            INSERT INTO accounts_metadata (name, group_id, birth_date) 
            VALUES (?, ?, ?)''', (account, group_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S") ), commit=True)
    else:
        execute('''
            INSERT INTO accounts_metadata (name, birth_date) 
            VALUES (?, ?)''', (account, datetime.now().strftime("%Y-%m-%d %H:%M:%S")), commit=True)
    return account

def create_group(name, parent_group=None)
    if parent_group != None:
        parent_id = get_id(parent_group, is_account=False)
        execute('''
        INSERT INTO groups (group_name, parent_group, birth_date) 
        VALUES (?, ?, ?)''', (name, parent_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S") ), commit=True)
    else:
        execute('''
        INSERT INTO groups (group_name, birth_date) 
        VALUES (?, ?)''', (name, datetime.now().strftime("%Y-%m-%d %H:%M:%S") ), commit=True)

def change_parent_group(name, parent_group, is_account=True) -> None:
    if is_account:
        id = get_id(name)
        execute('''
                UPDATE series_metadata
                SET group_id = (SELECT group_id FROM groups WHERE group_name = ?)
                WHERE account_id = ?;
            ''', (parent_group, id), commit=True)
    else:
        id = get_id(name, is_account=False)
        execute('''
                UPDATE groups
                SET parent_group = (SELECT group_id FROM groups WHERE group_name = ?)
                WHERE group_id = ?;
            ''', (parent_group, id), commit=True)



#coger los valores-tiempo de una cuenta o de varias
#insertar varios valores de golpe a una serie