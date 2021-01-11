import psycopg2


class User:
    def __init__(self, email, first_name, last_name, id_=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id_

    def __repr__(self):
        return "< User {} >".format(self.email)

    def create_table(self):
        connection = psycopg2.connect("dbname='learning' user='i-sip_iot' password='Your_Password'")
        cur = connection.cursor()
        try:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS "public"."users"(
                "id" SERIAL PRIMARY KEY,
                "email" character varying(255),
                "first_name" character varying(255),
                "last_name" character varying(255)
            )
            WITH (OIDS=FALSE);
            """)

            connection.commit()

            print("TABLE {} created".format('users'))

        except:
            print("Unable to craete the table!!!")

    def save_to_db(self):
        with psycopg2.connect("dbname='learning' user='i-sip_iot' password='Your_Password'") as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s);',
                                   (self.email, self.first_name, self.last_name))
                except:
                    print("Unable to add data")


    def fetch_data(self):
        connection = psycopg2.connect("dbname='learning' user='i-sip_iot' password='Your_Password'")
        cur = connection.cursor()
        try:
            cur.execute("SELECT * FROM users;")
            print(cur.fetchall())
        except:
            print("Failed to read the table contents ...")