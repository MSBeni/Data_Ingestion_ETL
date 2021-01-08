import psycopg2

try:
    conn = psycopg2.connect("dbname='pyapp' user='i-sip_iot' password='Your_Password'")
    print("Connected to the Database")
except:
    print("unable to connect to the database")


cur = conn.cursor()

try:
    cur.execute("SELECT * FROM customers;")

    print(cur.fetchall())
except:
    print("Failed to read the table contents ...")
