from mysql.connector import connect
import mysql

def create_database(database : str):
    conn = connect(host="localhost",user="root")
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {database}")

def mysql_connect(database : str):
    conn = connect(host="localhost",user="root",database=database)
    return conn

def connect_and_cursor(database : str):
    conn = mysql_connect(database)
    cursor = conn.cursor()
    return conn,cursor

def create_table(cursor : mysql.connector.cursor.MySQLCursor):
    cursor.execute("CREATE TABLE nfts (id INT primary key, token_id VARCHAR(255), name VARCHAR(255), top_bid VARCHAR(255), permalink VARCHAR(255)")

def insert_row(cursor, id, token_id, name, top_bid, permalink):
    cursor.execute(f"INSERT INTO fintechtask (id, token_id, name, top_bid, permalink) values ({id}, {token_id}, {name}, {top_bid}, {permalink})")

def insert_many_rows(cursor, values : list):
    cursor.executemany("INSERT INTO fintechtask (id, token_id, name, top_bid, permalink) values (%s, %s, %s, %s, %s)", values)

def setup_db(database):
    conn, cursor = connect_and_cursor(database)
    create_table(cursor)

    return conn,cursor

if __name__=="__main__":
    conn, cursor = connect_and_cursor("fintechtask")
    print(conn, type(cursor))