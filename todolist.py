tasks_list = []
completed_tasks = []
deleted_tasks = []

def add_task():
    user_task = input('Enter the task: ')
    tasks_list.append(user_task)

def view_tasks():
    for i, task in enumerate(tasks_list):
        if i == 0:
            print(f'The tasks list is following:')
            print(i+1, task)
        else:
            print(i+1, task)

def complete_task():
    if len(tasks_list) >= 0:
        view_tasks()
        com_task_num = int(input('Type the task number to move it to completed: '))
        com_task = tasks_list.pop(com_task_num-1)
        completed_tasks.append(com_task)
        print(f'The task {com_task} is moved to completed tasks list.')
        # view_tasks()
    else:
        print('The list is empty.')


def delete_task():
    view_tasks()
    del_task_num = int(input('Which task you want to delete: '))
    # task_to_del = tasks_list[del_task_num-1]
    task_to_del = tasks_list.pop(del_task_num -1)
    # del tasks_list[del_task_num-1]
    print(f'The task {task_to_del} is now deleted.')
    # view_tasks()

while True:
    user_choice = int(input('''Type the number of your choice:
                    1) Add Task
                    2) View Tasks
                    3) Complete Tasks
                    4) Delete Tasks
                    Your choice: '''))
    if user_choice == 1:
        add_task()
    elif user_choice == 2:
        view_tasks()
    elif user_choice == 3:
        complete_task()
    elif user_choice == 4:
        delete_task()
    else:
        print('Please provide the number of the give option correctly.')
    user_input = input('Do you want to continue? type y or n: ').lower()
    
    if user_input == 'n':
        break