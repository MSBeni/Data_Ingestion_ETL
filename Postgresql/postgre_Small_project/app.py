from Postgresql.postgre_Small_project.database import Database
from Postgresql.postgre_Small_project.users import User
# from Postgresql.postgre_Small_project.database import Database

Database.initialize()

user = User('frank@Uniofcode.me', 'Frank', 'Raykard')
# user.create_table()
user.save_to_db()
user.fetch_data()

user = User.load_from_db_by_email('jose@schoolofcode.me')
print(user)