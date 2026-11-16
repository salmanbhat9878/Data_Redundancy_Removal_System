import sqlite3

def add_record(name, email):
    if not name.strip() or not email.strip():
        print("Name and email cannot be empty!")
        return
    conn = sqlite3.connect("redundancy.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO records (name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
        print("Record added successfully!")

    except sqlite3.IntegrityError:
        print("Duplicate record detected! Email already exists.")

    finally:
        conn.close()


def show_records():
    conn = sqlite3.connect("redundancy.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()

    print("\nSaved Records:")
    for record in records:
        print(record)

    conn.close()


name = input("Enter your name: ").strip()
email = input("Enter your email: ").strip().lower()

if not name:
    print("Name cannot be empty!")

elif "@" in email and "." in email.split("@")[-1]:
    add_record(name, email)
    show_records()

else:
    print("Invalid email! Please enter a valid email.")