import psycopg2

try:
    conn = psycopg2.connect("dbname='learning' user='i-sip_iot' password='Your_Password'")
    print("Connected to the Database")
except:
    print("unable to connect to the database")


cur = conn.cursor()


# Table structure for customers
try:
    cur.execute("""
    DROP TABLE IF EXISTS "public"."users";
    CREATE TABLE "public"."users" (
        "id" SERIAL PRIMARY KEY,
        "email" character varying(255),
        "first_name" character varying(255),
        "last_name" character varying(255)
    )
    WITH (OIDS=FALSE);
    """)


    # cur.execute("INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s);", ('jose@schoolofcode.me', 'Jose', 'Salvatierra'))

    conn.commit()

    print("TABLE users created")

    cur.execute("SELECT * FROM users;")
    print(cur.fetchall())

except:
    print("Unable to craete the table!!!")
