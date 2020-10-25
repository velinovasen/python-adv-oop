from project.task import Task
from typing import List


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task Name: {new_task.name} - Due Date: {new_task.due_date} is added to the section"

    def complete_task(self, task_name: str):
        tasks_list = list(filter(lambda t: t.name == task_name, self.tasks))
        if tasks_list:
            curr_task = tasks_list[0]
            curr_task.completed = True
            return f"Completed task {curr_task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        completed_tasks = list(filter(lambda t: t.completed, self.tasks))
        for c_t in completed_tasks:
            self.tasks.remove(c_t)
        return f'Cleared {len(completed_tasks)} tasks.'

    def view_section(self):
        print_token = ""
        print_token += f'Section {self.name}:\n'
        for token in self.tasks:
            print_token += token.details() + "\n"
        return print_token
