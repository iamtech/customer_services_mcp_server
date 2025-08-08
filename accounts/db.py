import sqlite3

DB_PATH = "customer_data.db"

def get_db_conn():
    return sqlite3.connect(DB_PATH)

def get_customer_accounts(customer_id: int):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT account_id, account_name FROM accounts WHERE customer_id=?", (customer_id,))
    rows = cur.fetchall()
    conn.close()
    return [{"account_id": r[0], "account_name": r[1]} for r in rows]