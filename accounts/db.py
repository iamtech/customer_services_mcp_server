import sqlite3

DB_PATH = "../data/customer_data.db"

def get_db_conn():
    return sqlite3.connect(DB_PATH)

def get_customer_accounts(customer_id: str):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT account_id, account_type FROM accounts WHERE customer_id=?", (customer_id,))
    rows = cur.fetchall()
    conn.close()
    return [{"account_id": r[0], "account_type": r[1]} for r in rows]