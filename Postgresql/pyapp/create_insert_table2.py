import psycopg2

try:
    conn = psycopg2.connect("dbname='pyapp' user='i-sip_iot' password='Your_Password'")
    print("Connected to the Database")
except:
    print("unable to connect to the database")


cur = conn.cursor()


# Table structure for customers
try:
    cur.execute("""
        DROP TABLE IF EXISTS "public"."items";
        CREATE TABLE "public"."items" (
            "name" varchar(255) NOT NULL COLLATE "default",
            "id" int4 NOT NULL,
            "price" numeric(10,2)
        )
        WITH (OIDS=FALSE);
    """)

    cur.execute("INSERT INTO items VALUES (%s, %s, %s);", ('Pen', '1', '5.00'))
    cur.execute("INSERT INTO items VALUES (%s, %s, %s)", ('Fountain Pen', '2', '11.30'))
    cur.execute("INSERT INTO items VALUES (%s, %s, %s)", ('Ink', '3', '3.50'))
    cur.execute("INSERT INTO items VALUES (%s, %s, %s)", ('Laptop', '4', '899.00'))
    cur.execute("INSERT INTO items VALUES (%s, %s, %s)", ('Screen', '5', '275.50'))
    cur.execute("INSERT INTO items VALUES (%s, %s, %s)", ('Hard Drive', '6', '89.99'))

    conn.commit()

    print("TABLE items created")

except:
    print("Unable to craete the table!!!")
