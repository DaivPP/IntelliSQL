import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Define the extended Students table
create_table_query = """
CREATE TABLE IF NOT EXISTS Students (
    name TEXT NOT NULL,
    class TEXT NOT NULL,
    marks INTEGER NOT NULL,
    company TEXT,
    age INTEGER,
    email TEXT,
    placement TEXT
);
"""
cursor.execute(create_table_query)

# Insert sample records
students = [
    ('Sijo', 'BTech', 75, 'JSW', 21, 'sijo@example.com', 'Yes'),
    ('Aisha', 'MTech', 88, 'Infosys', 23, 'aisha@example.com', 'Yes'),
    ('Rahul', 'BSc', 62, None, 20, 'rahul@example.com', 'No'),
    ('Neha', 'MBA', 79, 'Deloitte', 24, 'neha@example.com', 'Yes'),
    ('Arjun', 'BTech', 55, None, 22, 'arjun@example.com', 'No'),
    ('Priya', 'BCom', 90, 'EY', 21, 'priya@example.com', 'Yes')
]

# Insert each record
cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?, ?)", students)

# Retrieve and print all records
df = cursor.execute("SELECT * FROM Students")
for row in df:
    print(row)

# Commit and close
conn.commit()
conn.close()

print("✅ Students table created, populated, and displayed.")
