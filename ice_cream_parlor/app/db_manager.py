import sqlite3

def setup_db():
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()

    # Create the flavors table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        allergens TEXT
    )
    """)

    # Create the cart table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_id INTEGER,
        FOREIGN KEY (flavor_id) REFERENCES flavors(id)
    )
    """)

    conn.commit()
    conn.close()
