import sqlite3

def add_flavor(name, description, allergens):
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO flavors (name, description, allergens)
    VALUES (?, ?, ?)
    """, (name, description, allergens))
    conn.commit()
    conn.close()

def search_flavors(keyword):
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM flavors WHERE name LIKE ?
    """, ('%' + keyword + '%',))
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def get_flavors():
    # Fetch all available flavors
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavors")
    flavors = cursor.fetchall()
    conn.close()
    return flavors
