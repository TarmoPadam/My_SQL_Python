from mysql.connector import connect, Error
from crud import create_database_query, create_tables_query, add_todo_list_query, create_item_to_list


def setup_db():
    try:
        with connect(host="localhost", user="root", password="MustangV62008", port="3306") as conn:
            with conn.cursor() as cursor:
                cursor.execute(create_database_query)
                cursor.execute("USE todo_app")
                cursor.execute(create_tables_query)

    except Error as e:
        print(e)


def create_todo_list(title):
    try:
        with connect(host="localhost", user="root", password="MustangV62008", port="3306", database="todo_app") as conn:
            with conn.cursor() as cursor:
                cursor.execute(add_todo_list_query(title))
                conn.commit()
    except Error as e:
        print(e)


def create_task(list_id, name):
    try:
        with connect(host="localhost", user="root", password="MustangV62008", port="3306", database="todo_app") as conn:
            with conn.cursor() as cursor:
                cursor.execute(create_item_to_list(list_id, name))
                conn.commit()



def select_tasks():
    try:
        with connect(host="localhost", user="root", password="MustangV62008", port="3306", database="todo_app") as conn:
            with conn.cursor() as cursor:
                cursor.execute(select_all_tasks_query)
                print(cursor.fetchall())


def delete_task(task_id):
    try:
        with connect(host="localhost", user="root", password="MustangV62008", port="3306", database="todo_app") as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_task_query(task_id))
                conn.commit()


    except Error as e:
        print(e)


if __name__ == "__main__":
    setup_db()
    # list_name = input("Enter the name of the list: ")
    # create_todo_list(list_name)

    #task_title = input("Task title: ")
    #create_task(1, task_title)
