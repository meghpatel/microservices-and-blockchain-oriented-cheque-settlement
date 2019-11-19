import sqlite3
from sqlite3 import Error
conn=sqlite3.connect('database.db')
print("Opened Successfully")

def create_connection(db_file):
	conn=None
	try:
		conn=sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return conn

def create_table(conn,table_detail):
	try:
		c=conn.cursor()
		c.execute(table_detail)
	except Error as e:
		print(e)

def main():
	database='database.db'
	user_table_attr=""" CREATE TABLE IF NOT EXISTS client(
		AC_NO Integer primary key,
		full_name TEXT NOT NULL UNIQUE,
	    email TEXT NOT NULL UNIQUE,
	    phone TEXT NOT NULL UNIQUE,
	    balance integer not null,
	    password text not null
	    );"""
	user_cheque_attr=""" CREATE TABLE IF NOT EXISTS user_cheque(
		AC_NO integer not null,
		cheque_id integer primary key,
		status text not null,
		FOREIGN KEY(AC_NO) REFERENCES client(AC_NO)
		);"""
	user_qr_attr=""" CREATE TABLE IF NOT EXISTS user_qr(
		qr_id integer primary key,
		qr_content text not null Unique,
		AC_NO integer not null,
		status text not null,
		FOREIGN KEY(AC_NO) REFERENCES client(AC_NO)
		);"""
	otp_attr="""CREATE TABLE IF NOT EXISTS otp_table(
		otp_id integer primary key,
		trans_id integer not null,
		otp integer not null,
		timestamp_val text not null,
		FOREIGN KEY(trans_id) REFERENCES sent_cheque(trans_id)
	);"""
	# transaction_attr=""" CREATE TABLE IF NOT EXISTS trans(
	# 	transaction_id integer primary key,
	# 	from_acc integer not null,
	# 	to_acc integer not null,
	# 	amt integer not null,
	# 	transaction_data text not null,
	# 	transaction_time text not null,
	# 	FOREIGN KEY(from_acc) REFERENCES client(AC_NO),
	# 	FOREIGN KEY(to_acc) REFERENCES client(AC_NO)
	# 	);"""

	sent_cheque_attr=""" CREATE TABLE IF NOT EXISTS sent_cheque(
		trans_id integer primary key,
		qr_id integer not null,
		sender_name text not null,
		receiver_name text not null,
		dated text not null,
		amount integer not null,
		sent_to_bank integer not null,
		FOREIGN KEY(receiver_name) REFERENCES client(full_name),
		FOREIGN KEY(qr_id) REFERENCES user_qr(qr_id),
		FOREIGN KEY(sender_name) REFERENCES client(full_name)
		);"""
	pending_attr="""CREATE TABLE IF NOT EXISTS pending(
		transaction_id integer primary key,
		sender_acc integer not null,
		receiver_acc integer not null,
		receiver_name text not null,
		sender_name text not null,
		dated text not null,
		amount integer not null,
		sender_qr text not null,
		transaction_date text not null,
		transaction_time text not null,
		FOREIGN KEY(sender_acc) REFERENCES client(AC_NO),
		FOREIGN KEY(receiver_acc) REFERENCES client(AC_NO),
		FOREIGN KEY(sender_name) REFERENCES client(full_name),
		FOREIGN KEY(receiver_name) REFERENCES client(full_name),
		FOREIGN KEY(sender_qr) REFERENCES client(qr_content)
		);"""

	conn=create_connection(database)
	if conn is not None:
		# create_table(conn,)
		create_table(conn,otp_attr)
		# create_table(conn,pending_attr)
		# create_table(conn,sent_cheque_attr)
		print("Successfully Created")
	else:
		print("NOT POSSIBLE to create")
	conn.close()

if __name__ == '__main__':
	main()