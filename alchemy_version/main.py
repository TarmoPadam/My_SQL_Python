import crud

if __name__ == "__main__":
    # list_name = input("Enter the name of the list: ")
    # crud.create_todo_list(list_name)

    # task_title = input("Task title: ")
    # crud.create_task(1, task_title)

    items_to_create = [{'name': 'Item1', 'list_id': 1},
                       {'name': 'Item2', 'list_id': 1}]
    crud.create_list_with_items('LIST1', items_to_create)

    lists = crud.select_lists()
    print(lists[0].items)
