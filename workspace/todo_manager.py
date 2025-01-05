from dataclasses import dataclass
from typing import List
from enum import Enum, auto

class TaskStatus(Enum):
    PENDING = auto()
    COMPLETED = auto()

@dataclass
class Task:
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING

class TodoManager:
    def __init__(self):
        self.tasks: List[Task] = []
    
    def add_task(self, title: str, description: str) -> None:
        """Add a new task to the list."""
        task = Task(title=title, description=description)
        self.tasks.append(task)
        print(f"Task added: {title}")
    
    def remove_task(self, title: str) -> None:
        """Remove a task by its title."""
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task removed: {title}")
                return
        print(f"Task not found: {title}")
    
    def mark_completed(self, title: str) -> None:
        """Mark a task as completed by its title."""
        for task in self.tasks:
            if task.title == title:
                task.status = TaskStatus.COMPLETED
                print(f"Task marked as completed: {title}")
                return
        print(f"Task not found: {title}")
    
    def display_tasks(self) -> None:
        """Display all tasks with their details."""
        if not self.tasks:
            print("No tasks found.")
            return
        
        print("\nTask List:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task.status == TaskStatus.COMPLETED else " "
            print(f"[{status}] {task.title}")
            print(f"    Description: {task.description}")
            print(f"    Status: {task.status.name}")
            print("-" * 50)

def main():
    todo = TodoManager()
    
    # Test the to-do list manager
    todo.add_task("Learn Python", "Study Python programming language basics")
    todo.add_task("Exercise", "Go to the gym for a workout")
    todo.add_task("Shopping", "Buy groceries for the week")
    
    todo.display_tasks()
    
    todo.mark_completed("Learn Python")
    todo.remove_task("Shopping")
    
    print("\nAfter marking one task as completed and removing another:")
    todo.display_tasks()

if __name__ == "__main__":
    main() 