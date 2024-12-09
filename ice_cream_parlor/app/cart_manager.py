import sqlite3

def add_to_cart(flavor_name):
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()

    # Get the flavor id from the name
    cursor.execute("SELECT id FROM flavors WHERE name=?", (flavor_name,))
    flavor_id = cursor.fetchone()

    if flavor_id:
        cursor.execute("INSERT INTO cart (flavor_id) VALUES (?)", (flavor_id[0],))
        conn.commit()
    conn.close()

def view_cart():
    conn = sqlite3.connect("ice_cream_parlor.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT flavors.name FROM cart
    JOIN flavors ON cart.flavor_id = flavors.id
    """)
    cart_items = cursor.fetchall()
    conn.close()
    return [item[0] for item in cart_items]
