import sqlite3

DB_FILE = "database.db"
SCHEMA_FILE = "schema.sql"

cnx = sqlite3.connect(DB_FILE)

with open(SCHEMA_FILE, "r") as f:
    cnx.executescript(f.read())

# Seed data
cnx.executescript("""
    INSERT INTO User (name, email) VALUES
        ('Alice', 'alice@example.com'),
        ('Bob',   'bob@example.com');

    INSERT INTO Post (title, body, user_id) VALUES
        ('Hello World',    'My first post.',   1),
        ('Second Post',    'More content.',    1),
        ('Bob''s Post',    'Bob writes too.',  2);
""")

cnx.commit()
cnx.close()

print(f"Database '{DB_FILE}' created and seeded successfully.")
