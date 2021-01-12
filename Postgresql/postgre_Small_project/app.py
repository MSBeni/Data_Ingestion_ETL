from Postgresql.postgre_Small_project.user import User
from Postgresql.postgre_Small_project.database import Database

user = User('Rado@newcode.me', 'Radolf', 'Bruno')
# user.create_table()
user.save_to_db()
user.fetch_data()

user = User.load_from_db_by_email('jose@schoolofcode.me')
print(user)