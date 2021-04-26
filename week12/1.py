import psycopg2

conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")

cur = conn.cursor()

cur.execute("SELECT * FROM sch1.users")

recordc = cur.fetchall()