import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data/portfolio.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create 'experience' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS experience (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        position TEXT NOT NULL,
        company TEXT NOT NULL,
        timeline TEXT NOT NULL,
        description TEXT
    )
''')

# Create 'education' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS education (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        degree TEXT NOT NULL,
        school TEXT NOT NULL,
        timeline TEXT NOT NULL
    )
''')

# Insert data into the 'experience' table
experience_data = [
    ("Intern", "Datametica Solutions Pvt. Ltd.", "Sep 2021 - Aug 2022"),
    ("Data Engineer", "Datametica Solutions Pvt. Ltd.", "Sep 2022 - Jul 2023"),
    ("Data Engineer Intern", "Onix", "May 2024 - Present")
]

cursor.executemany('''
    INSERT INTO experience (position, company, timeline)
    VALUES (?, ?, ?)
''', experience_data)

# Insert data into the 'education' table
education_data = [
    ("12th Computer Science", "Rajiv gandhi Jr. College of Science", "2016 - 2018"),
    ("Bachelors of Engineering in Computer Science", "Pimpri Chinchwad College of Engineering", "2018 - 2022"),
    ("MS in Computer Science", "San Jose State University", "2023 - 2025")
]

cursor.executemany('''
    INSERT INTO education (degree, school, timeline)
    VALUES (?, ?, ?)
''', education_data)

# Commit the changes and close the connection
conn.commit()

print("Tables 'experience' and 'education' created successfully.")


# Select and display all data from the 'experience' table
print("Experience Table Data:")
cursor.execute("SELECT * FROM experience")
experience_rows = cursor.fetchall()
for row in experience_rows:
    print(row)

# Select and display all data from the 'education' table
print("\nEducation Table Data:")
cursor.execute("SELECT * FROM education")
education_rows = cursor.fetchall()
for row in education_rows:
    print(row)

# Close the connection
conn.close()