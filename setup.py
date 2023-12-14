#!/usr/bin/env python
from setuptools import setup

setup(
    name="celery-scheduled-task-decorator",
    author="Dan Paulson",
    author_email="danpaulson@gmail.com",
    description="Decorator for scheduling tasks with celery",
    version='1.0.1',
    install_requires=[
        'celery',
    ]
)
