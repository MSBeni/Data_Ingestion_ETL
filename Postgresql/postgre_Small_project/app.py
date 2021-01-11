from Postgresql.postgre_Small_project.user import User
from Postgresql.postgre_Small_project.database import Database

user = User('john@schoolofcode.me', 'John', 'Malkovich')
user.create_table()
user.save_to_db()
user.fetch_data()