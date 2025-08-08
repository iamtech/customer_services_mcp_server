CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id TEXT NOT NULL,
    account_id TEXT NOT NULL,
    account_type TEXT NOT NULL
);

INSERT INTO accounts (customer_id, account_id, account_type) VALUES ('cust1', '1323124', 'savings');
INSERT INTO accounts (customer_id, account_id, account_type) VALUES ('cust1', '4325325', 'checking');
INSERT INTO accounts (customer_id, account_id, account_type) VALUES ('cust2', '6546774', 'savings');