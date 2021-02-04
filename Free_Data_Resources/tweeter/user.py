from database import CursorFromConnectionFromPool
from Free_Data_Resources.tweeter.tweeter_utils import consumer
import oauth2


class User:
    def __init__(self, email, first_name, last_name, oauth_token, oauth_token_secret, id_=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.id = id_

    # def __repr__(self):
    #     return self.oauth_token, self.oauth_token_secret

    @staticmethod
    def create_table():
        """
        Create database if it does not exist
        :return:
        """
        with CursorFromConnectionFromPool() as cursor:
            """
            Open and close the connection --> calling connection_pool.getconn() and after committing and closing the
            connection calling the connection_pool.putconn(self.connection) to put the connection in the pool
            """
            try:
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS "public"."usersauth"(
                    "id" SERIAL PRIMARY KEY,
                    "email" character varying(255),
                    "first_name" character varying(255),
                    "last_name" character varying(255),
                    "oauth_token" character varying(255),
                    "oauth_token_secret" character varying(255)
                )
                WITH (OIDS=FALSE);
                """)

                print("TABLE {} created".format('usersauth'))

            except:
                print("Unable to craete the table!!!")

    def save_to_db(self):
        """
        Save the inserted data into the database
        :return:
        """
        with CursorFromConnectionFromPool() as cursor:
            """
            Open and close the connection --> calling connection_pool.getconn() and after closing the
            connection calling the connection_pool.putconn(self.connection) to put the connection in the pool
            --> Note: ConnectionFromPool() is no longer a direct connection so does not commit any more using 'with'
            so we should add the commit to the ConnectionFromPool class
            """
            try:
                cursor.execute('INSERT INTO usersauth (email, first_name, last_name, oauth_token, oauth_token_secret) '
                               'VALUES (%s, %s, %s, %s, %s);',
                               (self.email, self.first_name, self.last_name, self.oauth_token, self.oauth_token_secret))
            except:
                print("Unable to add data")

    @staticmethod
    def fetch_data():
        """
        Executing the selection of inner data of the table
        :return:
        """
        with CursorFromConnectionFromPool() as cursor:
            """
            Open and close the connection --> calling connection_pool.getconn() and after committing and closing the
            connection calling the connection_pool.putconn(self.connection) to put the connection in the pool
            """
            try:
                cursor.execute("SELECT * FROM usersauth;")
                print(cursor.fetchall())
            except:
                print("Failed to read the table contents ...")

    @classmethod
    def load_from_db_by_email(cls, email):
        """
        Return a user form the database based on specific email address
        email :param str: the email address of the user seeking to return
        cls :return: cls a currently bound class od thw User
        """
        with CursorFromConnectionFromPool() as cursor:
            """
            Open and close the connection --> calling connection_pool.getconn() and after committing and closing the
            connection calling the connection_pool.putconn(self.connection) to put the connection in the pool
            """
            try:
                cursor.execute('SELECT * FROM usersauth WHERE email=%s', (email,))
                user_data = cursor.fetchone()
                # return user_data
                return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3],
                           oauth_token=user_data[4],  oauth_token_secret=user_data[5], id_=user_data[0])
            except:
                print("Problem in fetching data from db")


    def get_user_credentials(self, uri, verb):
        # Create an 'authorized_token' Token object and use that to perfoem Twitter API calls on behalf of the user
        authorized_token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        authorized_client = oauth2.Client(consumer, authorized_token)

        # Make Twitter API calls!
        response, content = authorized_client.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images'
            , 'GET')
        if response.status != 200:
            print('An error occurred while searching in twitter ...')
