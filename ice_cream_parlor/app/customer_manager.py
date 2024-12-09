from app.db_manager import connect_db

def add_customer_suggestion(flavor_suggestion, allergens):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customer_suggestions (flavor_suggestion, allergens) VALUES (?, ?)",
                       (flavor_suggestion, allergens))
        conn.commit()
