from Postgresql.postgre_Small_project.database import connection_pool


class User:
    def __init__(self, email, first_name, last_name, id_=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id_

    def __repr__(self):
        return "< User {} >".format(self.email)

    def create_table(self):
        with connection_pool.getconn() as connection:
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

                print("TABLE {} created".format('users'))

            except:
                print("Unable to craete the table!!!")

    def save_to_db(self):
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s);',
                                   (self.email, self.first_name, self.last_name))
                except:
                    print("Unable to add data")


    def fetch_data(self):
        with connection_pool.getconn() as connection:
            cur = connection.cursor()
            try:
                cur.execute("SELECT * FROM users;")
                print(cur.fetchall())
            except:
                print("Failed to read the table contents ...")

    @classmethod
    def load_from_db_by_email(cls, email):
        with connection_pool.getconn() as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute('SELECT * FROM users WHERE email=%s', (email,))
                    user_data = cursor.fetchone()
                    return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id_=user_data[0])
                except:
                    print("Problem in fetching data from db")
