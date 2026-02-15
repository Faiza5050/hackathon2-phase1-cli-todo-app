# todo_app/store.py
from .task import Task

class TaskStore:
    """In-memory collection of Task objects."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description: str) -> Task:
        task = Task(task_id=self.next_id, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Task | None:
        return next((t for t in self.tasks if t.id == task_id), None)

    def update_task(self, task_id: int, description: str) -> bool:
        task = self.get_task(task_id)
        if task:
            task.description = description
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def list_tasks(self) -> list[Task]:
        return self.tasks
