import sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()
# c.execute('insert into client values (1234567899,"Akul Agrawal","akulagrawal98@gmail.com",7096717330,5000,"akul")')
# c.execute('insert into client values (1234567890,"Naman Kabra","16bit004@nirmauni.ac.in",8032145682,5000,"naman")')
# c.execute('insert into client values (1234567880,"Megh Patel","meghpatel@gmail.com",8578213654,5000,"megh")')

c.execute('insert into user_qr values (1,"ABC",1234567880,"available")')
c.execute('insert into user_qr values (2,"DEF",1234567880,"available")')
c.execute('insert into user_qr values (3,"GHI",1234567890,"available")')
c.execute('insert into user_qr values (4,"JKL",1234567890,"available")')
c.execute('insert into user_qr values (5,"MNO",1234567899,"available")')
c.execute('insert into user_qr values (6,"PQR",1234567899,"available")')
c.execute('insert into user_qr values (7,"XYZ",1234567899,"available")')

# c.execute('insert into sent_cheque (qr_id,sender_name,receiver_name,dated,amount) values(5,"Akul Agrawal","Naman Kabra","4/08/2019",3000)')
conn.commit()