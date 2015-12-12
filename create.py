import sqlite3

conn = sqlite3.connect("blog.db")

c = conn.cursor()

q = "CREATE TABLE users(Username text, Password text, UserID integer)"
c.execute(q)

q = "CREATE TABLE blogs(Title text, Content text, BlogID integer, UserID integer)"
c.execute(q)

q = "CREATE TABLE comments(Content text, CommentID integer, BlogID integer, UserID integer)"
c.execute(q)

conn.commit() 
