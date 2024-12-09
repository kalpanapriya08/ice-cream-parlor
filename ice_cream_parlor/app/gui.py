import tkinter as tk
from tkinter import messagebox, ttk
from app.flavor_manager import add_flavor, search_flavors, get_flavors
from app.cart_manager import add_to_cart, view_cart
from app.db_manager import setup_db

def gui():
    # Initialize the database
    setup_db()

    # Create the main window
    root = tk.Tk()
    root.title("Ice Cream Parlor")
    root.geometry("850x650")
    root.config(bg="#fef7e2")  # Light pastel background color

    # Title label with a custom font
    title_label = tk.Label(root, text="Welcome to the Ice Cream Parlor", font=("Helvetica", 24, "bold"), bg="#fef7e2", fg="#3a3a3a")
    title_label.grid(row=0, column=0, columnspan=3, pady=20)

    # Cart Listbox and Cart Label
    cart_listbox = tk.Listbox(root, height=6, width=40, font=("Arial", 12), bd=0, bg="#fef7e2", selectbackground="#b3c2c2")
    cart_listbox.grid(row=1, column=1, padx=20, pady=10)
    cart_label = tk.Label(root, text="Your Cart", font=("Arial", 14, "bold"), bg="#fef7e2", fg="#3a3a3a")
    cart_label.grid(row=1, column=0, padx=10, pady=10)

    # Function to update the cart listbox
    def update_cart():
        cart_items = view_cart()
        cart_listbox.delete(0, tk.END)
        for item in cart_items:
            cart_listbox.insert(tk.END, item)

    def add_flavor_gui():
        def submit():
            name = name_entry.get()
            description = description_entry.get()
            allergens = allergens_entry.get()
            add_flavor(name, description, allergens)
            messagebox.showinfo("Success", "Flavor added successfully!")
            add_flavor_window.destroy()
            update_flavors_dropdown()

        add_flavor_window = tk.Toplevel(root)
        add_flavor_window.title("Add New Flavor")
        add_flavor_window.config(bg="#fef7e2")
        
        # Flavor Form with smooth input fields
        tk.Label(add_flavor_window, text="Flavor Name:", font=("Helvetica", 12), bg="#fef7e2").pack(pady=10)
        name_entry = tk.Entry(add_flavor_window, font=("Helvetica", 12), bd=2, relief="solid")
        name_entry.pack(pady=10)
        tk.Label(add_flavor_window, text="Description:", font=("Helvetica", 12), bg="#fef7e2").pack(pady=10)
        description_entry = tk.Entry(add_flavor_window, font=("Helvetica", 12), bd=2, relief="solid")
        description_entry.pack(pady=10)
        tk.Label(add_flavor_window, text="Allergens (comma-separated):", font=("Helvetica", 12), bg="#fef7e2").pack(pady=10)
        allergens_entry = tk.Entry(add_flavor_window, font=("Helvetica", 12), bd=2, relief="solid")
        allergens_entry.pack(pady=10)
        tk.Button(add_flavor_window, text="Submit", font=("Helvetica", 12), command=submit, bg="#90ee90", bd=0, relief="flat").pack(pady=20)

    def search_flavors_gui():
        def search():
            keyword = keyword_entry.get()
            flavors = search_flavors(keyword)
            flavor_dropdown['values'] = [flavor[1] for flavor in flavors]  # Update dropdown with search results

        search_window = tk.Toplevel(root)
        search_window.title("Search Flavors")
        search_window.config(bg="#fef7e2")
        tk.Label(search_window, text="Search for a Flavor:", font=("Helvetica", 12), bg="#fef7e2").pack(pady=20)
        keyword_entry = tk.Entry(search_window, font=("Helvetica", 12), bd=2, relief="solid")
        keyword_entry.pack(pady=10)
        tk.Button(search_window, text="Search", font=("Helvetica", 12), command=search, bg="#90ee90", bd=0, relief="flat").pack(pady=20)

    def add_to_cart_gui():
        selected_flavor = flavor_dropdown.get()
        if selected_flavor:
            add_to_cart(selected_flavor)
            update_cart()
            messagebox.showinfo("Success", f"{selected_flavor} added to cart!")
        else:
            messagebox.showwarning("Warning", "Please select a flavor.")

    def view_cart_gui():
        update_cart()
        cart_window = tk.Toplevel(root)
        cart_window.title("View Cart")
        cart_window.config(bg="#fef7e2")
        cart_items = view_cart()
        if cart_items:
            cart_text = tk.Text(cart_window, height=10, width=50, font=("Arial", 12), bd=2, relief="solid", bg="#fef7e2")
            cart_text.pack(padx=20, pady=10)
            for item in cart_items:
                cart_text.insert(tk.END, f"- {item}\n")
        else:
            messagebox.showinfo("Empty Cart", "Your cart is empty.")

    # Dropdown for selecting flavors with custom styling
    tk.Label(root, text="Select Flavor:", font=("Helvetica", 12), bg="#fef7e2", fg="#3a3a3a").grid(row=2, column=0, padx=10, pady=10)
    flavor_dropdown = ttk.Combobox(root, width=30, font=("Helvetica", 12), state="readonly")
    flavor_dropdown.grid(row=2, column=1, padx=10, pady=10)

    # Fetch all flavors initially to populate the dropdown
    def update_flavors_dropdown():
        flavors = get_flavors()
        flavor_dropdown['values'] = [flavor[1] for flavor in flavors]

    # Buttons with smooth design and responsive behavior
    button_style = {
        "font": ("Helvetica", 12),
        "width": 20,
        "height": 2,
        "bd": 0,
        "fg": "#ffffff",
        "bg": "#007bff",
        "relief": "flat",
    }
    tk.Button(root, text="Add Flavor", command=add_flavor_gui, **button_style).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(root, text="Search Flavors", command=search_flavors_gui, **button_style).grid(row=3, column=1, padx=10, pady=10)
    tk.Button(root, text="Add to Cart", command=add_to_cart_gui, **button_style).grid(row=4, column=0, padx=10, pady=10)
    tk.Button(root, text="View Cart", command=view_cart_gui, **button_style).grid(row=4, column=1, padx=10, pady=10)
    tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12), bg="#ff5733", fg="white", width=20, relief="flat").grid(row=5, column=1, padx=10, pady=10)

    # Start the main loop
    update_flavors_dropdown()  # Update dropdown with initial flavors
    root.mainloop()


if __name__ == "__main__":
    gui()
