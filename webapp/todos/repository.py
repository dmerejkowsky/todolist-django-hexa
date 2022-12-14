from task_manager.repository import Repository as BaseRepository
from task_manager.tasks import Task

from .models import Task as TaskModel


class Repository(BaseRepository):
    def add_task(self, description: str) -> None:
        TaskModel.objects.create(description=description, done=False)

    def update_task_status(self, id: int, done: bool) -> None:
        try:
            task = TaskModel.objects.get(id=id)
        except TaskModel.DoesNotExist:
            raise ValueError(f"No task with id {id}")
        task.done = done
        task.save()

    def remove_task(self, id: int) -> None:
        TaskModel.objects.get(id=id).delete()

    def tasks(self) -> list[Task]:
        return [
            Task(id=t.id, description=t.description, done=t.done)
            for t in TaskModel.objects.all()
        ]

    def load_tasks(self, tasks: list[Task]) -> None:
        for task in tasks:
            TaskModel.objects.create(
                id=task.id, description=task.description, done=task.done
            )
