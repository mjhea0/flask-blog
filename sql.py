import sqlite3

with sqlite3.connect("blog.db") as connection:
    # create cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE posts
             (title TEXT, post TEXT)
             """)

    # enter dummy data into table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m execellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
