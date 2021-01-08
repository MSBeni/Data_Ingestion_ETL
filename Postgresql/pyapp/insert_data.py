import psycopg2

try:
    conn = psycopg2.connect("dbname='pyapp' user='i-sip_iot' password='Your_Password'")
    print("Connected to the Database")
except:
    print("unable to connect to the database")


cur = conn.cursor()


# --  Records of customers

try:
    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", ('Jose', '2', 'Salvatierra'))
    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", ('Anne', '3', 'Watson'))
    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", ('Craig', '4', 'Scott'))
    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", ('Michael', '5', 'Adam'))
    conn.commit()
    print("Data is Added...")
except:
    print("Unable to add the data")

# ;
# INSERT INTO "public"."customers" VALUES ;
# INSERT INTO "public"."customers" VALUES ;
# INSERT INTO "public"."customers" VALUES ;
# INSERT INTO "public"."customers" VALUES ;


# --  Primary key structure for table customers

# ALTER TABLE "public"."customers" ADD PRIMARY KEY ("id") NOT DEFERRABLE INITIALLY IMMEDIATE;
