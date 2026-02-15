"""
Task model for the in-memory todo application.
Represents a single todo item with id, title, and completion status.
"""

class Task:
    """
    Represents a single todo item with attributes: ID, Description, IsCompleted.
    """

    def __init__(self, task_id: int, description: str, is_completed: bool = False):
        """
        Initialize a new Task instance.

        Args:
            task_id (int): Unique identifier for the task
            description (str): Description of the task
            is_completed (bool): Completion status of the task (default: False)
        """
        self.id = task_id
        self.description = description
        self.is_completed = is_completed

    def __str__(self):
        """
        String representation of the task.

        Returns:
            str: Formatted string showing task status and description
        """
        status = "✓" if self.is_completed else "○"
        return f"[{status}] {self.id}: {self.description}"

    def __repr__(self):
        """
        Developer-friendly representation of the task.

        Returns:
            str: Representation showing all attributes
        """
        return f"Task(id={self.id}, description='{self.description}', is_completed={self.is_completed})"