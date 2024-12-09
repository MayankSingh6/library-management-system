import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mayanksingh1@",  # Replace with your MySQL root password
    database="library_management"
)

cursor = connection.cursor()
print("Connected to the database!")

# Test query
cursor.execute("SHOW TABLES;")
for table in cursor:
    print(table)

# Close the connection
connection.close()


##################################

import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mayanksingh1@",
    database="library_management"
)

cursor = connection.cursor()



cursor.execute("""
    SELECT Borrower.borrower_id, Borrower.name, Book.title, Author.author_name, Category.category_name, Lending.issue_date, Lending.return_date
    FROM Borrower
    JOIN Lending ON Borrower.borrower_id = Lending.borrower_id
    JOIN Book ON Lending.book_id = Book.book_id
    JOIN Author ON Book.author_id = Author.author_id
    JOIN Book_Category ON Book.book_id = Book_Category.book_id
    JOIN Category ON Book_Category.category_id = Category.category_id
    WHERE Borrower.borrower_id = 'BR007';
""")
for detail in cursor.fetchall():
    print(detail)

