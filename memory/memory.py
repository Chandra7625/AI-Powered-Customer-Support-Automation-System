import sqlite3

conn = sqlite3.connect(
    "memory.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    query TEXT,
    response TEXT
)
""")

conn.commit()


def save_conversation(customer, query, response):

    cursor.execute(
        """
        INSERT INTO conversations
        (customer, query, response)
        VALUES (?, ?, ?)
        """,
        (customer, query, response)
    )

    conn.commit()


def get_last_issue(customer):

    cursor.execute(
        """
        SELECT query
        FROM conversations
        WHERE customer=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (customer,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return "No previous issue found."