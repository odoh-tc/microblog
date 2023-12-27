# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#  set FLASK_APP=microblog.py
# flask db init
# flask db migrate -m "users table
# flask db upgrade
# A foreign key, because it references a primary key of another table.
# flask db migrate -m "posts table"
# flask db upgrade
# >>> from app import app, db
# >>> from app.models import User, Post
# >>> import sqlalchemy as sa
# >>> app.app_context().push()
# >>> u = User(username='john', email='john@example.com')
# >>> db.session.add(u)
# >>> db.session.commit()
# >>> query = sa.select(User)
# >>> users = db.session.scalars(query).all()
# >>> users
# [<User john>, <User susan>]
#  u = db.session.get(User, 1)
# >>> p = Post(body='my first post!', author=u)
# >>> db.session.add(p)
# >>> db.session.commit()
# (venv) $ flask db downgrade base

# (venv) $ >>> query = sa.select(User).order_by(User.username.desc())
# >>> db.session.scalars(query).all()
# [<User susan>, <User john>]
# (venv) $ flask shell