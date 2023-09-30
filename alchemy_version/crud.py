from models import eng, TodoLists, TodoItems
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=eng)
session = Session()

# CREATE


def create_todo_list(title):
    session.add(TodoLists(title=title))
    session.commit()


def create_task(list_id, name):
    session.add(TodoItems(name=name, list_id=list_id))
    session.commit()


def create_list_with_items(title, items):
    list_with_items = TodoLists(title=title)
    for item in items:
        list_with_items.items.append(
            TodoItems(name=item['name'], list_id=item['list_id']))
    session.add(list_with_items)
    session.commit()


# READ


def select_tasks():
    return session.query(TodoItems).all()


def select_task(id):
    return session.query(TodoItems).where(TodoItems.item_id == id).first()


def select_lists():
    return session.query(TodoLists).all()


def select_list(id):
    return session.query(TodoLists).where(TodoLists.list_id == id).first()

# UPDATE


def make_complete(id):
    task = select_task(id)
    task.state = True
    session.commit()


def make_not_complete(id):
    task = select_task(id)
    task.state = False
    session.commit()

# DELETE


def delete_task(id):
    task = select_task(id)
    session.delete(task)
    session.commit()


def delete_list(id):
    list = select_list(id)
    session.delete(list)
    session.commit()