import sqlite3

# 1. Connecting to a database
with sqlite3.connect("example.db") as connection:
    cursor = connection.cursor()

    # 2. Creating a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    connection.commit()

    # 3. Inserting data into the table
    user_data = [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com')
    ]

    cursor.executemany('INSERT INTO users (username, email) VALUES (?, ?)', user_data)
    connection.commit()

    # 4. Querying data from the table
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    print("All Users:")
    for row in rows:
        print(row)

    # 5. Updating data in the table
    cursor.execute('UPDATE users SET email = ? WHERE username = ?', ('new_email@example.com', 'Alice'))
    connection.commit()

    # 6. Deleting data from the table
    cursor.execute('DELETE FROM users WHERE username = ?', ('Charlie',))
    connection.commit()

    # 7. Using context manager for transactions
    cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', ('David', 'david@example.com'))

    # 8. Using named placeholders
    new_user = ('Eve', 'eve@example.com')
    cursor.execute('INSERT INTO users (username, email) VALUES (:username, :email)',
                   {'username': new_user[0], 'email': new_user[1]})
    connection.commit()

    # 9. Handling errors
    try:
        cursor.execute('INSERT INTO users (username) VALUES (?)', ('ErrorUser',))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")

# 10. Closing the connection
connection.close()

# Note: For more complex databases or other database systems, you might need to use additional libraries or connect to a database server.
