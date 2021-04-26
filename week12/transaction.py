#!/usr/bin/python

import psycopg2

conn = None
try:
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # execute 1st statement
    cur.execute(statement_1)
    # execute 2nd statement
    cur.execute(statement_1)
    # commit the transaction
    conn.commit()
    # close the database communication
    cur.close()
except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        conn.close()