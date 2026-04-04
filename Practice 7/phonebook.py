# phonebook.py
import csv
from connect import get_conn

#Create table if it doesn't exist
def create_table():
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

#Insert from CSV
def insert_from_csv(file_path):
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (username, first_name, phone) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                (row['username'], row['first_name'], row['phone'])
            )
    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported successfully!")

#Insert from console
def insert_from_console():
    username = input("Введите уникальный username: ")
    first_name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO contacts (username, first_name, phone) VALUES (%s, %s, %s)",
            (username, first_name, phone)
        )
        conn.commit()
        print("Контакт добавлен!")
    except Exception as e:
        print(f"Ошибка добавления: {e}")
    finally:
        cur.close()
        conn.close()

#Update contact
def update_contact():
    username = input("Введите username для обновления: ")
    field = input("Что изменить? first_name или phone: ").lower()
    if field not in ["first_name", "phone"]:
        print("Неверное поле!")
        return
    new_value = input(f"Введите новое значение для {field}: ")
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    cur.execute(f"UPDATE contacts SET {field} = %s WHERE username = %s", (new_value, username))
    conn.commit()
    cur.close()
    conn.close()
    print("Контакт обновлён!")

#Query contacts
def query_contacts():
    print("Фильтровать по: 1. Имени 2. Префиксу телефона 3. Показать всё")
    choice = input("> ")
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    if choice == "1":
        name = input("Введите имя или часть имени: ")
        cur.execute("SELECT * FROM contacts WHERE first_name ILIKE %s", (f"%{name}%",))
    elif choice == "2":
        prefix = input("Введите префикс телефона: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
    else:
        cur.execute("SELECT * FROM contacts")
    results = cur.fetchall()
    if not results:
        print("Ничего не найдено.")
    else:
        for row in results:
            print(row)
    cur.close()
    conn.close()

#Delete contact
def delete_contact():
    target = input("Введите username или телефон для удаления: ")
    conn = get_conn()
    if not conn: return
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE username = %s OR phone = %s", (target, target))
    conn.commit()
    cur.close()
    conn.close()
    print("Контакт удалён (если существовал).")

#Main menu
if __name__ == "__main__":
    create_table()
    while True:
        print("\n1. Импорт CSV\n2. Добавить контакт\n3. Обновить контакт\n4. Поиск\n5. Удалить\n6. Выход")
        choice = input("Выберите опцию: ")
        if choice == "1":
            path = input("Путь к CSV файлу: ")
            insert_from_csv(path)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Неверный выбор!")