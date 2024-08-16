import sqlite3

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('students.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create the student_info table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT NOT NULL,
        major TEXT NOT NULL
    )
''')

# Step 4: Insert more than 10 records into the student_info table
students_data = [
    ('Alice Johnson', 20, 'Sophomore', 'Computer Science'),
    ('Bob Smith', 21, 'Junior', 'Mathematics'),
    ('Carol Davis', 19, 'Freshman', 'Biology'),
    ('David Brown', 22, 'Senior', 'Physics'),
    ('Eve Wilson', 20, 'Sophomore', 'Chemistry'),
    ('Frank Thompson', 21, 'Junior', 'Economics'),
    ('Grace Lee', 19, 'Freshman', 'English'),
    ('Henry Martinez', 22, 'Senior', 'History'),
    ('Irene Rodriguez', 20, 'Sophomore', 'Political Science'),
    ('Jack Wilson', 21, 'Junior', 'Philosophy'),
    ('Karen Young', 19, 'Freshman', 'Sociology'),
    ('Leo Harris', 22, 'Senior', 'Art History'),
    ('Mia Clark', 20, 'Sophomore', 'Music'),
    ('Nathan Lewis', 21, 'Junior', 'Psychology'),
    ('Olivia Hall', 19, 'Freshman', 'Anthropology')
]

# Step 5: Insert the data into the table
cursor.executemany('''
    INSERT INTO student_info (name, age, grade, major)
    VALUES (?, ?, ?, ?)
''', students_data)

# Commit the changes
conn.commit()

# Step 6: Write code to view the student_info table
cursor.execute('SELECT * FROM student_info')
rows = cursor.fetchall()

# Display the records
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}, Major: {row[4]}")

# Close the connection
conn.close()
