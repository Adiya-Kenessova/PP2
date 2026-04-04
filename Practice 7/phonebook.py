import csv
from connect import get_conn

# --- Create table ---
def create_table():
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# --- Insert from CSV ---
def insert_from_csv(file_path):
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                    (row['name'], row['phone'])
                )
        conn.commit()
        print("CSV imported successfully!")
    except Exception as e:
        print(f"Error importing CSV: {e}")
    finally:
        cur.close()
        conn.close()

# --- Insert from console ---
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Contact added!")
    except Exception as e:
        print(f"Error adding contact: {e}")
    finally:
        cur.close()
        conn.close()

# --- Update contact ---
def update_contact():
    phone = input("Enter phone of contact to update: ")
    new_name = input("Enter new name (leave empty to skip): ")
    new_phone = input("Enter new phone (leave empty to skip): ")
    
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    
    if new_name:
        cur.execute("UPDATE contacts SET name = %s WHERE phone = %s", (new_name, phone))
    if new_phone:
        cur.execute("UPDATE contacts SET phone = %s WHERE phone = %s", (new_phone, phone))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated!")

# --- Search contacts ---
def search_contacts():
    print("1. By name  2. By phone prefix  3. Show all")
    choice = input("Choose filter: ")
    
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    
    if choice == "1":
        name = input("Enter name or part of name: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name}%",))
    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
    else:
        cur.execute("SELECT * FROM contacts")
    
    rows = cur.fetchall()
    if not rows:
        print("No contacts found.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Phone':<15}")
        print("-" * 45)
        for row in rows:
            id_, name, phone = row
            print(f"{id_:<5} {name:<20} {phone:<15}")
    
    cur.close()
    conn.close()

# --- Delete contact ---
def delete_contact():
    phone = input("Enter phone of contact to delete: ")
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted (if it existed).")

# --- Main menu ---
if __name__ == "__main__":
    create_table()
    
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Import CSV")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Search contact")
        print("5. Delete contact")
        print("6. Show all contacts")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            path = input("Enter CSV file path: ")
            insert_from_csv(path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            search_contacts()  # show all
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
