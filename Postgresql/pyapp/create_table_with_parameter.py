import psycopg2
from psycopg2 import sql

try:
    conn = psycopg2.connect("dbname='pyapp' user='i-sip_iot' password='Your_Password'")
    print("Connected to the Database")
except:
    print("unable to connect to the database")


cur = conn.cursor()


# Table structure for customers
try:
    table_name = 'test_table'
    cur.execute(
        sql.SQL("""
                CREATE TABLE IF NOT EXISTS "public".{} (
                    "first_name" varchar(100) COLLATE "default",
                    "id" int4 NOT NULL,
                    "last_name" varchar(255) COLLATE "default"
                )
                WITH (OIDS=FALSE);""")
            .format(sql.Identifier(table_name)))

    cur.execute(
        sql.SQL("INSERT INTO {} VALUES (%s, %s, %s)")
            .format(sql.Identifier(table_name)),
        ['John', '12', 'Mensah'])

    conn.commit()

    print("TABLE {} created".format(table_name))

    cur.execute(sql.SQL("SELECT * FROM {};").format(sql.Identifier(table_name)))

    print(cur.fetchall())

except:
    print("Unable to craete the table!!!")
