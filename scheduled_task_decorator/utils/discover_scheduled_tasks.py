import importlib
import pkgutil


def discover_scheduled_tasks(package_name):
    package = importlib.import_module(package_name)
    tasks = {}
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, package_name + '.'):
        module = importlib.import_module(module_name)
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr) and hasattr(attr, '_celery_schedule'):
                task_name = getattr(attr, '_celery_task_name')
                tasks[task_name] = {
                    'task': task_name,
                    'schedule': getattr(attr, '_celery_schedule')
                }
    return tasks
