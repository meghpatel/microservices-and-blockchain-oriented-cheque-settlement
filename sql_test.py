import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()
c.execute('insert into client values (1234567899,"Akul","Agrawal","akulagrawal98@gmail.com",7096717330,5000,"akul")')
conn.commit()
conn.close()