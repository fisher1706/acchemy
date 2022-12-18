import sqlite3


conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

query_select = '''SELECT * FROM books'''
cur.execute(query_select)
rows = cur.fetchall()

print('ROW SQL query:', rows)


query_update = '''UPDATE books SET want_to_read = TRUE WHERE title = "The Hobbit"'''
cur.execute(query_update)
cur.execute(query_select)
rows = cur.fetchall()
                               
print('ROW SQL query:', rows)

conn.close()