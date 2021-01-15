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
        DROP TABLE IF EXISTS "public"."locations";
        CREATE TABLE "public"."locations" (
            "user_id" int4 NOT NULL,
            "pos_date" DATE NOT NULL,
            "pos_time" TIME NOT NULL,
            "x_pos"  numeric(10,4),
            "y_pos"  numeric(10,4)
        )
        WITH (OIDS=FALSE);
    """)

    cur.execute("INSERT INTO locations VALUES (%s, %s, %s, %s, %s);", ('96069608', '2021-01-13', '14:14:49.109766',
                                                                       '14.515996294097572', '2.8996316399675544'))
    cur.execute("INSERT INTO locations VALUES (%s, %s, %s, %s, %s)", ('96069608', '2021-01-15', '15:30:12.105256',
                                                                      '14.515996294097572', '2.8996316399675544'))

    conn.commit()

    print("TABLE items created")

    cur.execute("SELECT * FROM locations;")

    print(cur.fetchall())

    # "COPY locations TO 'locations.csv' DELIMITER ',' CSV HEADER;"
    # cur.execute("COPY locations TO '../locations.csv' DELIMITER (FORMAT CSV, HEADER);")

    outputquery = "COPY locations TO STDOUT WITH ',' CSV HEADER;"

    with open('resultsfile', 'w') as f:
        cur.copy_expert(outputquery, f)


except:
    print("Unable to craete the table!!!")
