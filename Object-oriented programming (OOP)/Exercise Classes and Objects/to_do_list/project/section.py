from typing import List

from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        tsk = next((t for t in self.tasks if t.name == task_name), None)
        if tsk:
            tsk.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        current_tasks_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f"Cleared {current_tasks_len - len(self.tasks)} tasks."

    def view_section(self) -> str:
        tasks_details = "\n".join([t.details() for t in self.tasks])
        return f"Section {self.name}:\n{tasks_details}"


