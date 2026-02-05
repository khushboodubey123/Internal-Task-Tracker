from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = 'tasks'
    def ready(self):
        from .schedulers import task_expire_scheduler
        task_expire_scheduler()
