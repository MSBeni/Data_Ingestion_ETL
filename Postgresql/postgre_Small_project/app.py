from Postgresql.postgre_Small_project.database import Database
from Postgresql.postgre_Small_project.users import User
import json

MY_PASS = json.loads(open('../../../secretfiles.json', 'r').read())['web']['user_pw']

Database.initialize(database='learning', user='i-sip_iot', password=MY_PASS, host='localhost')

user = User('muli@Uniofcode.me', 'Muli', 'Mossa')
# user.create_table()
user.save_to_db()
user.fetch_data()

user = User.load_from_db_by_email('jose@schoolofcode.me')
print(user)