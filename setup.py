import sqlite3

DB_FILE = "database.db"
SCHEMA_FILE = "schema.sql"

cnx = sqlite3.connect(DB_FILE)

with open(SCHEMA_FILE, "r") as schemafil:
    cnx.executescript(schemafil.read())

# Seed data
cnx.executescript("""
    INSERT INTO Highscores (name, score) VALUES 
    ('Testuser', '10'); 
""")

cnx.commit()
cnx.close()

print(f"Database '{DB_FILE}' created and seeded successfully.")
